#!/usr/bin/python

# Script to generate wiggle file
# Generate a wiggle track to identify segments that are:
#   >= 100 nt in length
#   Belong to class with >= 0.9 probability
#   Do I care about indels at this point? Probably not

# this requires scipy v 1.2.0 or greater
# 
# Dear me, please consider using proper code hygeine and writing actually informative comments.

import os, argparse, csv, re, subprocess
import numpy as np
from scipy.signal import find_peaks

parser = argparse.ArgumentParser()
parser.add_argument("-gpFile", "--groupFile", help="group profile", type = str)
parser.add_argument("-maf", "--mafFile", help="filtered .maf alignment", type = str) #should have 'filtered' prefix
parser.add_argument("-gt", "--groupThreshold", help="Threshold group profile positions", type = float, default=0.75)
parser.add_argument("-cpFile","--cpFile",help="Change point .cp file")

parser.add_argument("-o", "--output", help='name of output file', type = str)
# parser.add_argument("-ct", "--cPointThreshold",help="Threshold for change point positions", type = float, default = 0.5)

args = parser.parse_args()
segSize = 50 # Set this to be length of a seq in output file (apparently this doesn't fo anythign)

cpFile = args.cpFile
## Remove any temp giles that are present in the directory from previous analysis
if os.path.isfile(args.output) == True:
	os.remove(args.output)
if os.path.isfile('maf_gp_temp') == True:
	os.remove('maf_gp_temp')
if os.path.isfile('human_info_temp') == True:
	os.remove('human_info_temp')


subprocess.call('touch maf_gp_temp',shell=True)


## inits:
init_maxGapProp = 0.5
init_maxGapLen = 3
gt = args.groupThreshold
init_ct = 0.5
init_minSegLen = 6
## Get Sequence positions. 
## Generate file that has sequence positions taken from .net.axt
## format:
## no. chrom_in_ref pos_start pos_end other_org pos_start pos_end seq_len

# with open(args.mafFile) as f:
# 	with open('maf_gp_temp','w+') as g:
# 	    for dirtyProfileLine in f:
# 	    	cleanProfileLine = dirtyProfileLine.split()
# 	    	if len(cleanProfileLine) <= 2:
# 	    		pass
# 	    	elif 'hg19'in cleanProfileLine[1]:
# 	    		seqLen = int(cleanProfileLine[3])
# 	    		if seqLen > segSize:
# 	    			q = seqLen/segSize
# 	    			r = seqLen % segSize
# 	    			for i in range(1,q+1):
# 	    				seqStart = int(cleanProfileLine[2])+(i-1)*segSize
# 	    				writeString = "{},{},{}\n".format(cleanProfileLine[1],seqStart,segSize)
# 	    				g.write(writeString)
# 	    				if i == max(range(q+1)) and r != 0:
# 	    					seqStart = seqStart+segSize
# 	    					writeString = "{},{},{}\n".format(cleanProfileLine[1],seqStart,r)
# 	    					g.write(writeString)
# 	    		else:
# 	    			writeString = "{},{},{}\n".format(cleanProfileLine[1],cleanProfileLine[2],cleanProfileLine[3])
# 	    			g.write(writeString)

## Generate a file from .maf that only contains the human information
with open(args.mafFile, 'r') as f:
	with open('human_info_temp', 'w+') as g:
		for line in f:
			if 'hg19' in line:
				g.write(line)


# Returns True if segment is contains less than maxGapProp proportion of gaps
def fn_acceptableGapProp(seg,maxGapProp):

	if len(seg) == 0:
		return False
	else:
		gapProp = len(seg[seg<0])/float(len(seg))

		return gapProp < maxGapProp 

# Returns true if all non-gap positions are above profile threshold
def fn_profVal(seg,threshold):
	if len(seg) == 0:
		return False
	elif all(seg <= 0):
		return False
	else:
		valueBool = all(seg[seg>0] > threshold)
		return valueBool

# Returns true if length of seg is greater than minSegLen
def fn_checkLen(seg,minSegLen):
	
	if len(seg) == 0:
		return False
	else:	
		return len(seg) > minSegLen

# Returns true if segment contains at least one subset of indeces
# is made of maxGapLen number of adjacent elemnts
def fn_acceptableGapLen(seg,maxGapLen):
	boolArray = seg<0
	isThere_a_Gap = False
	segGapLocs = np.where(seg<0)[0]

	gapLocSet = set(segGapLocs)

	for i in segGapLocs:
		adjPos = range(i,i+maxGapLen+1)
		adjPosSet = set(adjPos)

		

		if adjPosSet.issubset(gapLocSet):
			isThere_a_Gap = adjPosSet.issubset(gapLocSet)
			break
	return not isThere_a_Gap

## Generate a file where lines alternate between indeces of sequence positions above threshold and 
## starting with profile values and then change point

with open(args.groupFile,'r') as f:
	with open(args.cpFile,'r') as g:
		with open('gp_and_cp_temp','w') as h:
			for rawGpLine,rawCpLine in zip(f,g):
				separator = ','

				gpValue = rawGpLine.rstrip().split(',')
				gpValue = gpValue[1:]

				cpValue = rawCpLine.rstrip().split(',')
				cpValue = cpValue[1:]

				h.write(separator.join(gpValue)+'\n')
				h.write(separator.join(cpValue)+'\n')
# the lines of the file that are created 
# can be read in as gpValueVec

with open('human_info_temp','r') as f:
	with open('gp_and_cp_temp','r') as g:
		with open(args.output,'w+') as h:
			for line in f:

				dirtyData = line.rstrip().split()
				speciesChorom = dirtyData[1]
				tempVar1 = speciesChorom.split('.')
				chromStart = int(dirtyData[2])
				justChrom = tempVar1[1]
				

				valueVec_gp = g.readline()
				valueVec_cp = g.readline()

				#as arrays

				gpValueVec = np.array(map(float,valueVec_gp.split(',')))
				cpValueVec = np.array(map(float,valueVec_cp.split(',')))

				#find the peaks of where change points occur
				changePoints, _ = find_peaks(cpValueVec,init_ct) 

				if len(changePoints) == 0:
					# check first position and last position
				
					lastPosVal = cpValueVec[-1]
					if lastPosVal > 0.5:
						# weird edge case of one long segment and one small segment at the end
						segCandidates = np.split(gpValueVec,np.array([0,len(gpValueVec)-1]))
						segCandidates = segCandidates[1:]
						tempVal = -2
						# edgeCase1 = True
						
					else: #one long segment
						segCandidates = np.split(gpValueVec,np.array([0,len(gpValueVec)]))
						segCandidates = segCandidates[1]
						tempVal = -1
						# edgeCase2 = True
				#split the gpValueVec into sub arrays that contain segments
				#delineated by change point boundaries

				else:
					segCandidates = np.split(gpValueVec,changePoints)
					tempVal = len(segCandidates)
					segStartSet = np.append([0],changePoints) 
					segEndSet = np.append(changePoints,[len(gpValueVec)])
				# print 'There are {} segments in this line\n'.format(abs(tempVal))

				# import pdb; 
				# if abs(tempVal) == 2:
				#     pdb.set_trace()
				# print segCandidates
				for i in range(abs(tempVal)):
					isFirst = True
					# print segCandidates[i]
					if tempVal == -1:
						# print segCandidates
						# print '\n'
						segStart = 0
						segEnd = len(segCandidates)
						seg = segCandidates
					elif tempVal == -2:
						seg = segCandidates
						segStart = 0
						segEnd = len(segCandidates)-1

					else:
						# import pdb; pdb.set_trace()
						seg = segCandidates[i]
						segStart = segStartSet[i]
						segEnd = segEndSet[i]
					# print 'this is seg {} on this line\n'.format(i)
					# print seg

					# print '\n less than 0.5 gaps {}\n'.format(fn_acceptableGapProp(seg,init_maxGapProp))
					
					# print 'are all positions > {}? {}\n'.format(gt,fn_profVal(seg,gt))
					
					# print 'is longer than {} positions? {}\n'.format(init_minSegLen,fn_checkLen(seg,init_minSegLen))
					
					# print 'are all gaps less than {} in length? {}\n'.format(init_maxGapLen,fn_acceptableGapLen(seg,init_maxGapLen))
					
					# import pdb; pdb.set_trace()
					#if we have all the criteria we care about the segment
					if (fn_acceptableGapProp(seg,init_maxGapProp) and
						fn_profVal(seg,gt) and
						fn_checkLen(seg,init_minSegLen) and
						fn_acceptableGapLen(seg,init_maxGapLen)):

						print seg
						if all(seg <= 0):
							print '\n less than 0.5 gaps {}\n'.format(fn_acceptableGapProp(seg,init_maxGapProp))
					
							print 'are all positions > {}? {}\n'.format(gt,fn_profVal(seg,gt))
					
							print 'is longer than {} positions? {}\n'.format(init_minSegLen,fn_checkLen(seg,init_minSegLen))
					
							print 'are all gaps less than {} in length? {}\n'.format(init_maxGapLen,fn_acceptableGapLen(seg,init_maxGapLen))

						bedChromStart = chromStart  + segStart
						bedChromEnd = chromStart + segEnd

						writeString = '{}\t{}\t{}\n'.format(justChrom,bedChromStart,bedChromEnd)
						h.write(writeString)


				# dirtyData = line.rstrip().split()
				# speciesChorom = dirtyData[1]
				# tempVar1 = speciesChorom.split('.')
				# chromStart = int(dirtyData[2])
				# justChrom = tempVar1[1]
				

				# valueVec_gp = g.readline()
				# valueVec_cp = g.readline()

				# #as arrays

				# gpValueVec = np.array(map(float,valueVec_gp.split(',')))
				# cpValueVec = np.array(map(float,valueVec_cp.split(',')))

				# #find the peaks of where change points occur
				# changePoints, _ = find_peaks(cpValueVec,init_ct) 

				# if len(changePoints) == 0:
				# 	# check first position and last position
				
				# 	lastPosVal = cp_line[-1]
				# 	if lastPosVal > 0.5:
				# 		# weird edge case of one long segment and one small segment at the end
				# 		segCandidates = np.split(profile_line,np.array([0,len(profile_line)-1]))
				# 		segCandidates = segCandidates[1:]
				# 		# edgeCase1 = True
						
				# 	else: #one long segment
				# 		segCandidates = np.split(profile_line,np.array([0,len(profile_line)]))
				# 		segCandidates = segCandidates[1]
				# 		# edgeCase2 = True
				# #split the gpValueVec into sub arrays that contain segments
				# #delineated by change point boundaries

				# else:
				# 	segCandidates = np.split(gpValueVec,peaks)

				# for i in range(len(segCandidates)):

				# 	if segCandidates
				# 	# #end edge case
				# 	# if i == len(changePoints):
				# 	# 	segStart = changePoints[i-1]
				# 	# 	segEnd = len()
				# 	# elif changePoints[i] == 0:
				# 	# 	segStart = -2
				# 	# 	segEnd = -2
				# 	# 	# this is the case where there is an empty segment
				# 	# # elif i==0;
				# 	# # 	segStart = 0
				# 	# # 	segEnd = changePoints[i]
				# 	# else:
				# 	# 	if i == 0:
				# 	# 		segStart = 0
				# 	# 	else:
					# 		segStart = changePoints[i-1]
					# 	segEnd = changePoints[i]

					# # if we have all the criteria we care about the segment
					# if (fn_acceptableGapProp(segCandidates[i],init_maxGapProp) and
					# 	fn_profVal(segCandidates[i],gt) and
					# 	fn_checkLen(segCandidates[i],init_minSegLen) and
					# 	fn_checkGapSize(segCandidates[i],init_maxGapLen)):

					# 	bedChromStart = chromStart  + segStart
					# 	bedChromEnd = chromStart + segEnd[0]

					# 	writeString = '{}\t{}\t{}\n'.format(justChrom,bedChromStart,bedChromEnd)
					# 	h.write(writeString)



# with open('human_info_temp','r') as f:
# 	with open(args.groupFile,'r') as g:
# 		with open(args.output,'w+') as h: 
# 			for line in g: #corresponds to an alignment block

# 				# produce an np array of numeric
# 				valueVec = line.rstrip().split(',')
# 				valueVec = valueVec[1:]
# 				valueVec = np.array(map(float,valueVec))

# 				#find positions that are above threshold
# 				indexVec = np.where(valueVec > t)[0]
# 				diffVec = np.diff(indexVec)
# 				#find positions where gaps are in the block
# 				gapLocation = np.where(diffVec > 6)[0]
					
# 				if len(indexVec) == 0:
# 					pass
# 					#no segments above threshold in this line. Need to advance human data.dirtyData
# 					dirtyData = f.readline().rstrip().split()

# 				elif len(gapLocation) == 0:
# 					#only one segment in the line
# 					#positions of segment starts
# 					segStart = np.insert(indexVec[gapLocation + 1],0,0)
# 					#positions of segment ends
# 					segEnd = np.insert(indexVec[gapLocation],len(indexVec[gapLocation]),max(indexVec))

# 					dirtyData = f.readline().rstrip().split()

# 					speciesChorom = dirtyData[1]
# 					tempVar1 = speciesChorom.split('.')
# 					chromStart = int(dirtyData[2])
# 					justChrom = tempVar1[1]
					

# 					bedChromStart = chromStart  + segStart[0]
# 					bedChromEnd = chromStart + segEnd[0] + 1
					
# 					writeString = '{}\t{}\t{}\n'.format(justChrom,bedChromStart,bedChromEnd)
# 					h.write(writeString)

# 				# # if there are gaps => multiple segments in the line
# 				elif len(gapLocation) > 0:
					
# 					# print 'more than one segment in block \n'
# 					#positions of segment starts
# 					segStart = np.insert(indexVec[gapLocation + 1],0,0)
# 					#positions of segment ends
# 					segEnd = np.insert(indexVec[gapLocation],len(indexVec[gapLocation]),max(indexVec))
# 					delVec = np.array([])	

# 					# Collect positions for segments that are <6 in len
# 					for i in range(len(segStart)):
# 						segLen = segEnd[i] - segStart[i]
# 						# if segLen > 50:
# 						# 	print 'segment size = {}'.format(segLen)
# 						if segLen < 6:
# 							delVec = np.insert(delVec,0,i)
# 					# delete those segments
# 					delVec = delVec.astype(int)
# 					segStart = np.delete(segStart,delVec)
# 					segEnd = np.delete(segEnd,delVec)

# 					dirtyData = f.readline().rstrip().split()
# 					speciesChorom = dirtyData[1]
# 					tempVar1 = speciesChorom.split('.')
# 					justChrom = tempVar1[1]
# 					chromStart = int(dirtyData[2])
					
# 					for j in range(len(segStart)):
# 						bedChromStart = chromStart + segStart[j]
# 						bedChromEnd = chromStart + segEnd[j] + 1 # +1 because interval is [start,end)
# 						writeString = '{}\t{}\t{}\n'.format(justChrom,bedChromStart,bedChromEnd)

						# h.write(writeString)

						# print writeString

command = 'sort -o {} {}'.format(args.output,args.output)
subprocess.call(command,shell=True)
## Delete temp files		
# uncomment this section at the end 
os.remove('human_info_temp')
os.remove('maf_gp_temp')

