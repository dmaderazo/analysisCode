# master file containing all python functions required for change point analysis
import os 
import subprocess
import numpy as np
import argparse
import glob
import pandas as pd
# Encoding function

# def encoding(inputFile,outputFile):
	

#   if inputFile[-3:] == 'axt':
#       #Do 2 way encoding
#       if os.path.isfile(outputFile) == True:
#           os.remove(outputFile)
#   elif inputFile[-3:] == 'maf':
#       pass
#       #Do 3 way
#   else:
#       print 'Error: Check input file types are .net.axt or .maf.'
# function to identify proportion of string made up of elements of bad letters 
# def char_prop(word):
#     # THIS IS CASE SENSITIVE
#     # These letters are deifinitely ignored by changepoint
#     badSet = {'I','J','K','L','M','N','#'}
#     word_len = float(len(word))
#     char_count = 0

#     for c in word:
#         if c in badSet:
#             char_count += 1

#     return (char_count/word_len) 
#     #this function is required to filter out 'bad' segments in the en

def do_2_way(org1,org2):
	outSeq = ''
	for c,d in zip(org1,org2):
		if c == '-':
			# remove gaps
			pass
		elif c == 'A' and d == 'A':
			outSeq += 'a'
		elif c == 'A' and d == 'C':
			outSeq += 'b'
		elif c == 'A' and d == 'G':
			outSeq += 'c'
		elif c == 'A' and d == 'T':
			outSeq += 'd'
		elif c == 'C' and d == 'A':
			outSeq += 'e'
		elif c == 'C' and d == 'C':
			outSeq += 'f'
		elif c == 'C' and d == 'G':
			outSeq += 'g'
		elif c == 'C' and d == 'T':
			outSeq += 'h'
		elif c == 'G' and d == 'A':
			outSeq += 'i'
		elif c == 'G' and d == 'C':
			outSeq += 'j'
		elif c == 'G' and d == 'G':
			outSeq += 'k'
		elif c == 'G' and d == 'T':
			outSeq += 'l'
		elif c == 'T' and d == 'A':
			outSeq += 'm'
		elif c == 'T' and d == 'C':
			outSeq += 'n'
		elif c == 'T' and d == 'G':
			outSeq += 'o'
		elif c == 'T' and d == 'T':
			outSeq += 'p'    
		elif d == '-':
			outSeq += 'I'
		outSeq += '#'
	return outSeq

def do_3_way(org1,org2,org3):
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
		# find the set of letters in outSeq
	wordSet = set(outSeq)

	#if the word is made up entirely of bad characters discard 
	if wordSet <= badSet:
		return None
	#This is necessary for change point input.

	# if the word is too short discard
	## ASK JON ABOUT THIS. Do I do this before or after?
	elif len(outSeq) < 7:
		return None
	# if the word is made up of mostly gaps, discard
	#elif char_prop(outSeq) > 0.5:
	 #   return None
	else: #return outSeq
		return outSeq

def encoding(inputFile,outputFile):
	#check extension of input file:
	newBed = 'filtered_'+inputFile

	ext = os.path.splitext(inputFile)[-1].lower()

	if os.path.isfile(outputFile):
		os.remove(outputFile)

	if os.path.isfile(newBed):
		os.remove(newBed)

	if ext == '.maf':

		with open(inputFile) as foo:
			with open(outputFile, 'a+') as bar:
				with open(newBed,'a+') as foobar:
					foobar.write('##maf version=1')   
					foobar.write('\n') 
					isFirstPass = 1

					for line in foo:

						if '##maf' in line:
							# foobar.write(line) #write header line
							pass
						
						if len(line) == 1:
							pass #do nothing with empty lines

						if line[0] == 'a': #store the score lines
							 aLine = line

						if line[0] == 's':
							# do things where the we have 's'pecies lines
							# create a list where each of the entries are the bits of information in the .maf file

							pre_dirt_1 = line
							dirtyLine_1 = pre_dirt_1.upper().split(' ')
							org1 = list(filter(lambda thing: thing != '', dirtyLine_1))
							org1_seq = org1[6] #this is just where the sequence part lives after filtering
							
							#same for species 2
							pre_dirt_2 = foo.next()
							dirtyLine_2 = pre_dirt_2.upper().split(' ')
							org2 = list(filter(lambda thing: thing != '', dirtyLine_2))
							org2_seq = org2[6]

							#same for spliecies 3
							pre_dirt_3 = foo.next()
							dirtyLine_3 = pre_dirt_3.upper().split(' ')
							org3 = list(filter(lambda thing: thing != '', dirtyLine_3))
							org3_seq = org3[6]
							
							# do encoding
							encodedBlock = do_3_way(org1_seq,org2_seq,org3_seq)
							# write to file if we care about the block
							if encodedBlock != None:
								foobar.write(aLine)
								foobar.write(pre_dirt_1)
								foobar.write(pre_dirt_2)
								foobar.write(pre_dirt_3)
								foobar.write('\n')
							# while countLine < lineCount:
							#     encodedBlock += '#'
							# write to temp file
							if encodedBlock == None:
								pass
							elif isFirstPass == 1:
								bar.write(encodedBlock)
								isFirstPass = 0
							elif isFirstPass != 1:
								bar.write('#'+encodedBlock)
		
def file_len(fname):
	p = subprocess.Popen(['wc', '-l', fname], stdout=subprocess.PIPE, 
											  stderr=subprocess.PIPE)
	result, err = p.communicate()
	if p.returncode != 0:
		raise IOError(err)
	return int(result.strip().split()[0])

def seg_len(start,end):
	return end - start

def classification(queryBed,refBed,threshold):
	queryFileLength = file_len(queryBed)
	
	# create storage array for results
	classifierOut = [None]*queryFileLength

	
	with open(queryBed, 'r') as f:
		index = 0
		for line in f:
			storage = line.split()
			chromosomeLocation = storage[0]
			queryStart = int(storage[1])
			queryEnd = int(storage[2])
			querySegLen = queryEnd - queryStart
			overlapProportion = 0
			with open(refBed,'r') as g:


				for refLine in g:
					storage2 = refLine.split()
					totalOverlapProportion = 0
					# overlapProportion = 0

					if storage[0] != chromosomeLocation: #look somewhere else
						pass
					else: #then go finer search
						refStart = int(storage2[1])
						refEnd = int(storage2[2])
						refSegLen = refEnd - refStart

						# print 'queryStart = {}\nqueryEnd = {}\nrefStart = {}\nrefEnd = {}\n'.format(queryStart,queryEnd,refStart,refEnd)


						if queryStart < refStart: 
						 	if queryEnd <= refStart:

								# print('miss1')

								pass 
								#we've missed
								# Q |-|
								# R     |-|
								#overlapProportion = 0 #asdas
							elif queryEnd >= refEnd:
							
								# print 'overlap1'
								#db.set_trace()
								#we have the following overlap
								# Q |-----|
								# R  |--|
								overlapProportion = refSegLen/float(querySegLen)
							elif  queryEnd < refEnd:
								# print 'overlap2'
								#we have the following overlap
								# Q |-----|
								# R    |-----|
								overlapProportion = (queryEnd-refStart)/float(querySegLen)
						elif queryStart >= refStart:
							if queryStart >= refEnd:
								# print 'miss2'
								pass
								#we've missed
								# Q      |--| 
								# R |--|
								#overlapProportion = 0
							elif queryEnd > refEnd:
								# print 'overlap3'
								#we have the following overlap
								# Q   |-----|
								# R |-----|
								overlapProportion = (refEnd-queryStart)/float(querySegLen)
								# print overlapProportion
							elif queryEnd <= refEnd:
								# print 'overlap 4'
								#we have the following overlap
								# Q   |-----|
								# R |---------|
								overlapProportion = 1.0
								# print overlapProportion
						
						# if overlapProportion == 0:
						# 	pass
						# else:
						# 	print 'overlapProportion = {}'.format(overlapProportion)
						# if overlapProportion < 0:

						totalOverlapProportion = totalOverlapProportion + overlapProportion

						# if totalOverlapProportion > 0:
						# 	print 'totalOverlapProportion = {}'.format(totalOverlapProportion)
							# pdb.set_trace()
				if totalOverlapProportion > threshold:
					# print totalOverlapProportion
					classifierOut[index] = 1
				else:
					# print totalOverlapProportion
					classifierOut[index] = 0

				# print classifierOut
				# print 'line passed'
						
			index += 1          
	print classifierOut
	outDf = pd.DataFrame({refBed:classifierOut})
	return outDf
	##########
	##
	## Idea: make the output of these write to a temp file and then write anlother function that takes those and then gets the required 
	## format for BUGS 
	##
	##########


	#### Need to write a function to identify most conserved class

	### A function to run jobs?


def isfloat(value):
  try:
	float(value)
	return True
  except ValueError:
	return False

def getLnDataframe(logFrameName):
	if os.path.isfile('temp.csv'):
		os.remove('temp.csv')
	logFileList = glob.glob('*.log')
	isFirst = True

	for file in logFileList:
		
			with open(file) as foo:
				firstLine = foo.readline().split()
				numGroups = str(firstLine[firstLine.index('-ng')+1])
				numGroups_index = 'sim_'+numGroups
				numIts = float(firstLine[firstLine.index('-n')+1])

				# store these things into a df
				storageFrame = pd.DataFrame([numGroups_index,numGroups,numIts])

				# iterate through each line of the file to obtain lnLikelihood
				# print 'this is the start of the line loop'
				for line in foo:
					splitLine = line.split()
					lnLikelihoodValue = splitLine[-1]

					# print lnLikelihoodValue
					# print isfloat(lnLikelihoodValue)
					singleItemFrame = pd.DataFrame([lnLikelihoodValue])



					if isfloat(splitLine[0]):
						storageFrame = pd.concat([storageFrame,singleItemFrame],ignore_index=True)

						# print storageFrame

				if isFirst:
					storageFrame.to_csv('temp.csv',index=False,header=False) # Need to turn off option for row index and header
					isFirst = False
				else:
					data = pd.read_csv('temp.csv',header=None)
					data_df = pd.concat([data,storageFrame],sort=False,axis=1)
					data_df.to_csv('temp.csv',index=False,header=False)
	# read in new df
	final_df = pd.read_csv('temp.csv',header=0)

	final_df = final_df.reindex(sorted(final_df.columns),axis=1)

	final_df.to_csv(logFrameName,index=False,header=True)
	os.remove('temp.csv')
	# os.rename('temp.csv',logFrameName)
				# print isFirst
				# print storageFrame
				# print 'this is the end of line loop'		
						# else:
						# 	# data = pd.read_csv('temp.csv')
						# 	storageFrame = pd.concat([storageFrame,singleItemFrame],sort=False)
						# 	data_df = pd.concat([data,storageFrame],sort=False,axis=1)
						# 	data_df.to_csv(logFrameName) # Need to turn off option for row index and header

#def getCharFreqs(outCsvFrame,alignment,threshold):
		

# What would I like the classification function to do:
#   take 3 inputs: queryBed,refBed, threshold
#       for each line in queryBed, identify if 
#       the segment represented by that line is present
#       in the refBed file (greater than threshold)
#       return a binary array containing the outcomes

#       Bonus: what if I want non-overlap?


