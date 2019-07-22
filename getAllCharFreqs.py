#!/anaconda2/bin/python
import os
import pandas as pd
import numpy as np 
import glob
import linecache
import argparse
import csv
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument("-gt", "--groupThreshold", help="Threshold group profile positions", type = float, default=0.75)
parser.add_argument("-encodedFile", "--encodedFile", help="Alignment encoding", type = str)
parser.add_argument('-o','--outputFile',help = 'Name of outputFile. saves with .csv extension',type = str)
args = parser.parse_args()
# x = [0]*462 
# myArray = np.array(x).reshape(14,33)
myCommand = "tr '#' '\n' < {} > encodingTemp".format(args.encodedFile)
os.system(myCommand)
profileList = glob.glob('*burnin.p*')

def dict_merge(dict1,dict2):
	result = {key: dict1.get(key,0) + dict2.get(key,0) for key in set(dict1) | set(dict2)}
	return result

def div_d(my_dict):
	sump_p = sum(my_dict.values())

	result = {}

	for i in my_dict:
		result[i] = my_dict[i]/float(sump_p)

	return result

def check_freq(string):
	freq = {}
	alphabet = 'abcdefghijklmnopqrstuvwxyzUVWXYZ'
	charList = list(alphabet)
	for c in charList:
		freq[c] = string.count(c)
	return freq


alphabet = 'abcdefghijklmnopqrstuvwxyzUVWXYZ'
charList = list(alphabet)
isFirst = True


for myProfile in profileList:
	print 'Processing file: {}'.format(myProfile)
	with open(myProfile, 'r') as foo:
		# inits
		storageRow = 0
		rowIndex = 1
		myFile = csv.reader(foo)
		countTemp = dict.fromkeys(charList,0)
		bigTotal = 0
		for line in myFile:
			clean_line = list(map(float,line[1:]))
			myArray = np.array(clean_line) # an array of group values

			# find indeces where values are greater than threshold
			indeces = list(np.where(myArray>args.groupThreshold)[0])
			# get encoded string as a list
			tempLine = linecache.getline('encodingTemp',rowIndex).strip()
			lineList = list(tempLine)

			# characters that are above threshold
			shortList = [lineList[i] for i in indeces]
			if len(shortList) == 0:
				pass
			else:
				mySeq = ''.join(shortList)
				counts = check_freq(mySeq)
				smallTotal = sum(counts.values())
				bigTotal = bigTotal+smallTotal

				countTemp = dict_merge(countTemp,counts)
			linecache.clearcache()
			rowIndex = rowIndex + 1
		groupCount = countTemp

		groupProp = div_d(groupCount)
		x = pd.DataFrame.from_dict([groupProp])
	if isFirst:
		myFrame = x
		isFirst = False
	else:
		myFrame = myFrame.append(x, ignore_index = True)


name = args.outputFile 

nameList = [name+'_'+i.split('.')[-1] for i in profileList]
# This is the final frame that has groups listed
myFrame.insert(0,'GroupFile',nameList,True)

myFrame.to_csv(name+'.csv',index = False,header=True)





