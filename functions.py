# master file containing all python functions required for change point analysis
import os 
import subprocess
import numpy as np
# Encoding function

def encoding(inputFile,outputFile):
	

	if inputFile[-3:] == 'axt':
		#Do 2 way encoding
		if os.path.isfile(outputFile) == True:
			os.remove(outputFile)

			
    os.remove(outputFile)
	elif inputFile[-3:] == 'maf'
		#Do 3 way
	else:
		print 'Error: Check input file types are .net.axt or .maf.'

def file_len(fname):
    p = subprocess.Popen(['wc', '-l', fname], stdout=subprocess.PIPE, 
                                              stderr=subprocess.PIPE)
    result, err = p.communicate()
    if p.returncode != 0:
        raise IOError(err)
    return int(result.strip().split()[0])

def classification(queryBed,refBed):
	queryFileLength = file_len(queryBed)

	# create storage array for results
	classifierOut = np.empty([queryFileLength,1])


	with open(queryBed, 'r') as f:
		index = 0
		for line in f:
			storage = line.split()
			chromosomeLocation = storage[0]
			queryStart = int(storage[1])
			queryEnd = int(storage[2])
			querySegLen = segEnd - segStart
			with open(refBed,'r') as g:
				for refLine in g:
					storage2 = refLine.split()
					if storage[0] != chromosomeLocation: #look somewhere else
						pass
					else: #then go finer search
						refStart = int(storage2[1])
						refEnd = int(storage2[2])
						refSegLen = refEnd - refStart
						if queryStart < refStart: 
							if queryEnd < refStart:
								pass 
								#we've missed
								# Q |-|
								# R 	|-|
							elif queryEnd > refEnd:
								#we have the following overlap
								# Q |-----|
								# R  |--|
								overlapProportion = refSegLen/float(querySegLen)

							elif  queryEnd < refEnd:
								#we have the following overlap
								# Q |-----|
								# R    |-----|
								overlapProportion = (queryEnd-refStart)/float(querySegLen)
						elif queryStart > refStart:
							if queryStart > refEnd:
								pass
								#we've missed
								# Q      |--| 
								# R |--|
							elif queryEnd > refEnd:
								#we have the following overlap
								# Q   |-----|
								# R |-----|
								overlapProportion = (queryStart - refEnd)/float(querySegLen)
							elif queryEnd < refEnd:
								#we have the following overlap
								# Q   |-----|
								# R |---------|
								overlapProportion = 1.0
						
						print overlapProportion

						if overlapProportion > threshold:
							classifierOut[index] = 1
						else:
							classifierOut[index] = 0

			index += 1			

# What would I like the classification function to do:
# 	take 3 inputs: queryBed,refBed, threshold
# 		for each line in queryBed, identify if 
# 		the segment represented by that line is present
# 		in the refBed file (greater than threshold)
# 		return a binary array containing the outcomes

# 		Bonus: what if I want non-overlap?


