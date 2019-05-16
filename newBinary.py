# new binary classification. Trying to make things quicker

# steps
# 1) Take query file (all beds) and reference file (sorted sites)
# 2) do bedops --element-of in order to get elements of Q in R > S
# 3) for line in Q, if in S, return 1.

# 

import functions as fn 
import os 
import argparse
import csv
import pandas as pd
from collections import Counter
import glob
import re
import subprocess
import numpy as np

def file_len(fname):
	p = subprocess.Popen(['wc', '-l', fname], stdout=subprocess.PIPE, 
											  stderr=subprocess.PIPE)
	result, err = p.communicate()
	if p.returncode != 0:
		raise IOError(err)
	return int(result.strip().split()[0])


parser = argparse.ArgumentParser()
# The order of stuff in bed file:
# justChrom bedChromStart bedChromEnd cgContent consProp
parser.add_argument('-i','--input',help='sorted group file in .bed format')
parser.add_argument('-o','--output',help='name of output .csv file')
parser.add_argument("-t", "--overlapThresh", 
	help="overlap threshold",type = float,default=0)
parser.add_argument('-cons','--cons',help='conservation threshold',
	type=float,default=0.5)
parser.add_argument('-cg','--cg',help='cg threshold',
	type=float,default=0.5)
args = parser.parse_args()
queryFile = args.input 
outputFile = args.output
t = args.overlapThresh
cons_threshold = args.cons
cg_threshold = args.cg


isFirst = True
queryLen = file_len(queryFile)
# Parameter block:
if t == 0:
	p = '1'
else:
	p = str(t*100)+'%'

# glob in the relevant reference files: 
# (need to be in directory where this is run)
refList=glob.glob('sorted_*')

# will store output in temp.
if os.path.isfile('temp.csv'):
	os.remove('temp.csv')

for refFile in refList:
	# create a temp file with the output of bedops of:
	# segments that are in Q and have overlap in R
	bedOpStr = ('bedops -e {} {} {} > temp.bed').format(p,queryFile,refFile)
	os.system(bedOpStr)

	grepStr = ('grep -nxf temp.bed {} | cut -f1 -d:').format(queryFile)

	out = subprocess.check_output(grepStr,shell=True)
	tempvar = out.strip().split('n')
	os.remove('temp.bed')

	storage = np.array([0]*queryLen)

	if tempvar[0] == '':
		pass
	else:
	# import pdb; pdb.set_trace()
	# the indeces of all the rows of qFile that should be 0
		outList = [int(i)-1 for i in out.strip().split('\n')]

		#Create a storage structure that is all 1's and replace with 0 for outList
		
		storage[outList] = 1
	df_data = pd.DataFrame({refFile:storage.tolist()})


	if isFirst:
		df_data.to_csv('temp.csv',index=False,header=True)
		isFirst=False
	else:
		storageDf=pd.read_csv('temp.csv',header=0)
		newDf=pd.concat([storageDf,df_data],axis=1)
		newDf.to_csv('temp.csv',index=False,header=True)

# still have to do cons and CG
line_count = 0
cg_cons_out = [None]*(queryLen)

fo = open(queryFile,'r')
for line in fo:
	temp = line.strip().split('\t')
	cg_prop = float(temp[3])
	cons_prop = float(temp[4])
	if (cons_prop > cons_threshold and cg_prop > cg_threshold):
		cg_cons_out[line_count] = 1
	else:
		cg_cons_out[line_count] = 0
	line_count += 1


cg_df = pd.DataFrame({'cons+CG':cg_cons_out})
storageDf=pd.read_csv('temp.csv',header=0)
newDf=pd.concat([storageDf,cg_df],axis=1)
newDf.to_csv('temp.csv',index=False,header=True)

fo.close()

final_df = pd.read_csv('temp.csv',header=0)
final_df.to_csv(outputFile,index=False,header=True)

os.remove('temp.csv')





