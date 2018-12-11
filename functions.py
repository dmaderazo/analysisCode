# master file containing all python functions required for change point analysis
import os 
import subprocess
import numpy as np
import argparse

# Encoding function

# def encoding(inputFile,outputFile):
	

# 	if inputFile[-3:] == 'axt':
# 		#Do 2 way encoding
# 		if os.path.isfile(outputFile) == True:
# 			os.remove(outputFile)
# 	elif inputFile[-3:] == 'maf':
# 		pass
# 		#Do 3 way
# 	else:
# 		print 'Error: Check input file types are .net.axt or .maf.'
# function to identify proportion of string made up of elements of bad letters 
def char_prop(word):
    # THIS IS CASE SENSITIVE
    # These letters are deifinitely ignored by changepoint
    badSet = {'I','J','K','L','M','N','#'}
    word_len = float(len(word))
    char_count = 0

    for c in word:
        if c in badSet:
            char_count += 1

    return (char_count/word_len) 
def encoding_2_way(org1,org2):
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

def encoding_3_way(org1,org2,org3):
    #Define our bad letters
    badSet = {'I','J','K','L','M','N'}
   
    outSeq = ''
    for c,d,e in zip(org1,org2,org3):
        if c == '-' and d == '-' and e =='-': #(000)
            pass
        elif c != '-' and d == '-' and e =='-':
            outSeq += 'N' #(100)
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
	if os.path.isfile(outputFile) == False:
    	pass
	else:
    	os.remove(outputFile)

    if os.path.isfile(newBed) == False:
    	pass
	else:
    	os.remove(newBed)


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
	queryFileLength = file_len(queryBed)+1
	
	# create storage array for results
	classifierOut = np.empty([queryFileLength,1])

	
	with open(queryBed, 'r') as f:
		index = 0
		for line in f:
			storage = line.split()
			chromosomeLocation = storage[0]
			queryStart = int(storage[1])
			queryEnd = int(storage[2])
			querySegLen = queryEnd - queryStart
			with open(refBed,'r') as g:
				for refLine in g:
					storage2 = refLine.split()
					totalOverlapProportion = 0
					if storage[0] != chromosomeLocation: #look somewhere else
						pass
					else: #then go finer search
						refStart = int(storage2[1])
						refEnd = int(storage2[2])
						refSegLen = refEnd - refStart
						if queryStart < refStart: 
							if queryEnd <= refStart:
								pass 
								#we've missed
								# Q |-|
								# R 	|-|
							elif queryEnd >= refEnd:
								#we have the following overlap
								# Q |-----|
								# R  |--|
								overlapProportion = refSegLen/float(querySegLen)

							elif  queryEnd < refEnd:
								#we have the following overlap
								# Q |-----|
								# R    |-----|
								overlapProportion = (queryEnd-refStart)/float(querySegLen)
						elif queryStart >= refStart:
							if queryStart >= refEnd:
								pass
								#we've missed
								# Q      |--| 
								# R |--|
							elif queryEnd > refEnd:
								#we have the following overlap
								# Q   |-----|
								# R |-----|
								overlapProportion = (queryStart - refEnd)/float(querySegLen)
							elif queryEnd <= refEnd:
								#we have the following overlap
								# Q   |-----|
								# R |---------|
								overlapProportion = 1.0
						
						totalOverlapProportion = totalOverlapProportion + overlapProportion

						if totalOverlapProportion >= threshold:
							classifierOut[index] = 1
						else:
							classifierOut[index] = 0

			index += 1			
	print classifierOut
	return classifierOut


# What would I like the classification function to do:
# 	take 3 inputs: queryBed,refBed, threshold
# 		for each line in queryBed, identify if 
# 		the segment represented by that line is present
# 		in the refBed file (greater than threshold)
# 		return a binary array containing the outcomes

# 		Bonus: what if I want non-overlap?


