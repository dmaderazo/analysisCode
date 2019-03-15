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

def my_3_way(org1,org2,org3):
	badSet = {'I','J','K','L','M','N'}
	outSeq = ''
	for c,d,e in zip(org1,org2,org3):
		if c == '-' and d == '-' and e =='-': #(000)
			pass
		elif c != '-' and d == '-' and e =='-':
			outSeq += 'N'     #(100)
		elif c != '-' and d == '-' and e !='-':
			outSeq += 'L' #(101)
		elif c != '-' and d != '-' and e =='-':
			outSeq += 'K' #(110)
		elif c == '-' and d != '-' and e !='-':
			outSeq += 'J' #(011)
		elif c == '-' and d == '-' and e !='-':
			outSeq += 'M' #(001)
		elif c == '-' and d != '-' and e =='-':
			outSeq += 'I'   #(010)
		elif (c == 'A' and d == 'A' and e == 'A') or (c == 'T' and d == 'T' and e == 'T'):
			outSeq += 'a'
		elif (c == 'A' and d == 'A' and e == 'C') or (c == 'T' and d == 'T' and e == 'G'):
			outSeq += 'b'
		elif (c == 'A' and d == 'A' and e == 'G') or (c == 'T' and d == 'T' and e == 'C'):
			outSeq += 'c'
		elif (c == 'A' and d == 'A' and e == 'T') or (c == 'T' and d == 'T' and e == 'A'):
			outSeq += 'd'
		elif (c == 'A' and d == 'C' and e == 'A') or (c == 'T' and d == 'G' and e == 'T'):
			outSeq += 'e'
		elif (c == 'A' and d == 'C' and e == 'C') or (c == 'T' and d == 'G' and e == 'G'):
			outSeq += 'f'
		elif (c == 'A' and d == 'C' and e == 'G') or (c == 'T' and d == 'G' and e == 'C'):
			outSeq += 'g'
		elif (c == 'A' and d == 'C' and e == 'T') or (c == 'T' and d == 'G' and e == 'A'):
			outSeq += 'h'
		elif (c == 'A' and d == 'G' and e == 'A') or (c == 'T' and d == 'C' and e == 'T'):
			outSeq += 'i'
		elif (c == 'A' and d == 'G' and e == 'C') or (c == 'T' and d == 'C' and e == 'G'):
			outSeq += 'j'
		elif (c == 'A' and d == 'G' and e == 'G') or (c == 'T' and d == 'C' and e == 'C'):
			outSeq += 'k'
		elif (c == 'A' and d == 'G' and e == 'T') or (c == 'T' and d == 'C' and e == 'A'):
			outSeq += 'l'
		elif (c == 'A' and d == 'T' and e == 'A') or (c == 'T' and d == 'A' and e == 'T'):
			outSeq += 'm'
		elif (c == 'A' and d == 'T' and e == 'C') or (c == 'T' and d == 'T' and e == 'G'):
			outSeq += 'n'
		elif (c == 'A' and d == 'T' and e == 'G') or (c == 'T' and d == 'A' and e == 'C'):
			outSeq += 'o'
		elif (c == 'A' and d == 'T' and e == 'T') or (c == 'T' and d == 'A' and e == 'A'):
			outSeq += 'p'
		elif (c == 'C' and d == 'A' and e == 'A') or (c == 'G' and d == 'T' and e == 'T'):
			outSeq += 'q'
		elif (c == 'C' and d == 'A' and e == 'C') or (c == 'G' and d == 'T' and e == 'G'):
			outSeq += 'r'
		elif (c == 'C' and d == 'A' and e == 'G') or (c == 'G' and d == 'T' and e == 'C'):
			outSeq += 's'
		elif (c == 'C' and d == 'A' and e == 'T') or (c == 'G' and d == 'T' and e == 'A'):
			outSeq += 't'
		elif (c == 'C' and d == 'C' and e == 'A') or (c == 'G' and d == 'G' and e == 'T'):
			outSeq += 'u'
		elif (c == 'C' and d == 'C' and e == 'C') or (c == 'G' and d == 'G' and e == 'G'):
			outSeq += 'v'
		elif (c == 'C' and d == 'C' and e == 'G') or (c == 'G' and d == 'G' and e == 'C'):
			outSeq += 'w'
		elif (c == 'C' and d == 'C' and e == 'T') or (c == 'G' and d == 'G' and e == 'A'):
			outSeq += 'x'
		elif (c == 'C' and d == 'G' and e == 'A') or (c == 'G' and d == 'C' and e == 'T'):
			outSeq += 'y'
		elif (c == 'C' and d == 'G' and e == 'C') or (c == 'G' and d == 'C' and e == 'C'):
			outSeq += 'z' 
		elif (c == 'C' and d == 'G' and e == 'G') or (c == 'G' and d == 'C' and e == 'C'):
			outSeq += 'U'
		elif (c == 'C' and d == 'G' and e == 'T') or (c == 'G' and d == 'C' and e == 'A'):
			outSeq += 'V'
		elif (c == 'C' and d == 'T' and e == 'A') or (c == 'G' and d == 'A' and e == 'T'):
			outSeq += 'W'
		elif (c == 'C' and d == 'T' and e == 'C') or (c == 'G' and d == 'A' and e == 'G'):
			outSeq += 'X'
		elif (c == 'C' and d == 'T' and e == 'G') or (c == 'G' and d == 'A' and e == 'C'):
			outSeq += 'Y'
		elif (c == 'C' and d == 'T' and e == 'T') or (c == 'G' and d == 'A' and e == 'A'):
			outSeq += 'Z'
	return outSeq


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
mafFile = args.mafFile
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

	

	# if seq_end-seq_start < 6:
	# 	small_seg_count+=1

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
		tempStorage[i] = my_3_way(spec1_seq,spec2_seq,spec3_seq)

	encoded_sequence = ''.join(tempStorage)
	cg_prop = get_CG_proportion(encoded_sequence)
	cons_prop = get_cons_prop(encoded_sequence)

	if (cons_prop > cons_threshold and cg_prop > cg_threshold):
		cg_out[line_count] = 1
	else:
		cg_out[line_count] = 0
	line_count += 1
	os.remove('mafTemp.maf')
	linecache.clearcache()
cg_df = pd.DataFrame({'cons+CG':cg_out})
storageDf=pd.read_csv('temp.csv',header=0)
newDf=pd.concat([storageDf,df_data],axis=1)
newDf.to_csv('temp.csv',index=False,header=True)

fo.close()

final_df = pd.read_csv('temp.csv',header=0)
final_df.to_csv(outputFile,index=False,header=True)

os.remove('temp.csv')






	



