import functions as fn 
import os 
import argparse
import csv
import pandas as pd
from collections import Counter
import glob
import re
import linecache

# Parameter block
cg_threshold = 0.4
cons_threshold = 0.6




def count_chars(s,chars):
	counter = Counter(s)
	return {c : counter.get(c,0) for c in chars}

def get_CG_proportion(seq):
	temp = 'qrstuvwxyzUVWXYZ' #specific to humans in 3 way alignment
	list_CG = list(temp)
	num_CG = sum(count_chars(seq,list_CG).values())
	return num_CG/float(len(seq))

def get_cons_prop(seq):
	list_cons = ['a','v'] #This is specific to humans in the 3 way alignment
	num_cons = sum(count_chars(seq,list_cons).values)
	return num_cons/float(len(seq))

parser = argparse.ArgumentParser()

parser.add_argument('-i','--input',help='sorted group file in .bed format')
parser.add_argument('-o','--output',help='name of output .csv file')
parser.add_argument("-maf", "--mafFile", help="filtered .maf alignment", 
					type = str)


args = parser.parse_args()
inputFile = args.input
outputFile = args.output
queryList=glob.glob('sorted_*')

isFirst = True

if os.path.isfile('temp.csv'):
	os.remove('temp.csv')

for queryFile in queryList:
	df_data=fn.classification(inputFile,queryFile,0.5)
	
	if isFirst:
		df_data.to_csv('temp.csv',index=False,header=True)
		isFirst=False
	else:
		storageDf=pd.read_csv('temp.csv',header=0)
		newDf=pd.concat([storageDf,df_data],axis=1)
		newDf.to_csv('temp.csv',index=False,header=True)

# This black creates another .maf file that allows mafExtractor usage
output = 'pm_'+mafFile
with open(mafFile,'r') as f:
	with open(output,'w+') as g:
		for line in f:
			whole_line = re.split(r'(\S+)',line)
			if len(whole_line) > 1:
				if whole_line[1] == 's':
					whole_line[9] = '+'
				writeString = ''.join(whole_line)

				# print writeString
			else:
				writeString = '\n'
			g.write(writeString)

numLines = fn.file_len(inputFile)
cg_out = [None]*numLines

fo = open(inputFile,'r')
line_count = 0
for line in fo:
	temp = line.split()
	chr_location = 'hg19.'+temp[0]
	seq_start = int(temp[1])
	seq_end = int(temp[2])
	print seq_end-seq_start

	

	if seq_end-seq_start < 6:
		small_seg_count+=1

	command_string = 'mafExtractor --maf pm_filtered_chr1_filtered_3way.maf '+\
		'--seq {} --start {} --stop {}'.format(chr_location,seq_start,seq_end) +\
		'> mafTemp.maf'
	os.system(command_string)

	# with open('mafTemp.maf','r') as foo:
	# 	with open('countFile','w+') as bar:
	# 		for line in foo:
	# 			if 'hg19' in line:
	# 				bar.write(line)

	num_blocks = (fn.file_len('mafTemp.maf')-2)//5

	tempStorage = [0]*num_blocks
	for i in range(len(tempStorage)):
		spec1_seq = linecache.getline('mafTemp.maf',5*(i+1)-1)  
		spec2_seq = linecache.getline('mafTemp.maf',5*(i+1)-1)
		spec3_seq = linecache.getline('mafTemp.maf',5*(i+1)+1)
		tempStorage[i] = fn.do_3_way(spec1_seq,spec2_seq,spec3_seq)

	encoded_sequence = ''.join(tempStorage)
	cg_prop = get_CG_proportion(encoded_sequence)
	cons_prop = get_cons_prop(encoded_sequence)

	if (cons_prop > cons_threshold and cg_prop > cg_threshold):
		cg_out[line_count] = 1
	else:
		cg_out[line_count] = 0
	line_count += 1
	os.remove('mafTemp.maf')
	
cg_df = pd.DataFrame({'cons+CG':cg_out})
storageDf=pd.read_csv('temp.csv',header=0)
newDf=pd.concat([storageDf,df_data],axis=1)
newDf.to_csv('temp.csv',index=False,header=True)

fo.close()

final_df = pd.read_csv('temp.csv',header=0)
final_df.to_csv(outputFile,index=False,header=True)

os.remove('temp.csv')






	



