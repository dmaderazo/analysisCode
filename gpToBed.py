#!/usr/bin/python

# Script to generate wiggle file
# Generate a wiggle track to identify segments that are:
#   >= 100 nt in length
#   Belong to class with >= 0.9 probability
#   Do I care about indels at this point? Probably not


# 
# Dear me, please consider using proper code hygeine and writing actually informative comments.

import os, argparse, csv, re, subprocess
import numpy as np
parser = argparse.ArgumentParser()
parser.add_argument("-gpFile", "--groupFile", help="group profile", type = str)
parser.add_argument("-maf", "--mafFile", help="filtered .maf alignment", type = str) #should have 'filtered' prefix
parser.add_argument("-t", "--threshold", help="Threshold", type = float, default=0.75)
parser.add_argument("-o", "--output", help='name of output file', type = str)

args = parser.parse_args()
segSize = 50 # Set this to be length of a seq in output file
t = args.threshold

## Remove any temp giles that are present in the directory from previous analysis
if os.path.isfile('maf_gp_temp') == True:
    os.remove('maf_gp_temp')
if os.path.isfile('human_info_temp') == True:
	os.remove('human_info_temp')


subprocess.call('touch maf_gp_temp',shell=True)
## Get Sequence positions. 
## Generate file that has sequence positions taken from .net.axt
## format:
## no. chrom_in_ref pos_start pos_end other_org pos_start pos_end seq_len

with open(args.mafFile) as f:
	with open('maf_gp_temp','w+') as g:
	    for dirtyProfileLine in f:
	    	cleanProfileLine = dirtyProfileLine.split()
	    	if len(cleanProfileLine) <= 2:
	    		pass
	    	elif 'hg19'in cleanProfileLine[1]:
	    		seqLen = int(cleanProfileLine[3])
	    		if seqLen > segSize:
	    			q = seqLen/segSize
	    			r = seqLen % segSize
	    			for i in range(1,q+1):
	    				seqStart = int(cleanProfileLine[2])+(i-1)*segSize
	    				writeString = "{},{},{}\n".format(cleanProfileLine[1],seqStart,segSize)
	    				g.write(writeString)
	    				if i == max(range(q+1)) and r != 0:
	    					seqStart = seqStart+segSize
	    					writeString = "{},{},{}\n".format(cleanProfileLine[1],seqStart,r)
	    					g.write(writeString)
	    		else:
	    			writeString = "{},{},{}\n".format(cleanProfileLine[1],cleanProfileLine[2],cleanProfileLine[3])
	    			g.write(writeString)

## Generate a file from .maf that only contains the human information
with open(args.mafFile, 'r') as f:
	with open('human_info_temp', 'w+') as g:
		for line in f:
			if 'hg19' in line:
				g.write(line)


with open('human_info_temp','r') as f:
	with open(args.groupFile,'r') as g:
		with open(args.output,'w+') as h: 
			for line in f: #get human data
				dirtyData = line.rstrip().split()
				# print dirtyData
				speciesChorom = dirtyData[1]
				chromStart = int(dirtyData[2])
				for line in g: #corresponds to an alignment block
					# produce an np array of numeric
					valueVec = line.rstrip().split(',')
					valueVec = valueVec[1:]
					valueVec = np.array(map(float,valueVec))

					#find positions that are above threshold
					indexVec = np.where(valueVec > t)[0]
					diffVec = np.diff(indexVec)
					#find positions where gaps are in the block
					gapLocation = np.where(diffVec > 6)[0]
					
					# if there are gaps => multiple segments in the class
					if len(gapLocation) > 0:
						#positions of segment starts
						segStart = np.insert(indexVec[gapLocation + 1],0,0)
						#positions of segment ends
						segEnd = np.insert(indexVec[gapLocation],len(indexVec[gapLocation]),max(indexVec))
						delVec = np.array([])	

						# Collect positions for segments that are <6 in len
						for i in range(len(segStart)):
							segLen = segEnd[i] - segStart[i]
							if segLen > 50:
								print 'segment size = {}'.format(segLen)
							if segLen < 6:
								delVec = np.insert(delVec,0,i)
						# delete those segments
						delVec = delVec.astype(int)
						segStart = np.delete(segStart,delVec)
						segEnd = np.delete(segEnd,delVec)
						
						for j in range(len(segStart)):
							bedChromStart = chromStart + segStart[j]
							bedChromEnd = chromStart + segEnd[j] + 1 # +1 because interval is [start,end)
							writeString = '{} {} {}\n'.format(speciesChorom,bedChromStart,bedChromEnd)

							h.write(writeString)

## Delete temp files		
# uncomment this section at the end 
# os.remove('human_info_temp')
# os.remove('maf_gp_temp')

	    		# writeString = "{},{},{}\n".format(cleanProfileLine[1],cleanProfileLine[2],cleanProfileLine[3])
    			# g.write(writeString)
        # species = lines[1]
        # if 'hg19' in species:
        	# print('yes')
                # print(lines[0])
                # cleanLines = lines.split(' ')
                # fleeb.write(lines)

# create file with sequence positions in ref organism (just numbers)
# with open('tempFile','r') as thing:
#     with open('thisTest','w+') as blah:
#         for line in thing:
#             axtLine = line.split()
#             startNum = int(axtLine[2])
#             endNum = int(axtLine[3])
#             sequencePositions = range(startNum,endNum + 1)
#             seqPos = ','.join(map(repr,sequencePositions))


#             blah.write('{}\n'.format(seqPos))


#writes a wiggle track 
#format
#Seq_pos profile value (how to filter?)
# with open('thisTest','r') as f:
#     with open(args.groupfile, 'r') as g:
#         with open(args.output,'w+') as h:
#             gpData = csv.reader(g)
#             seqPos = csv.reader(f)
            
#             for line1,line2 in zip(gpData,seqPos):
#                 cleanLines = np.array(np.float_(line1[1:]))
#                 seqPosPre = np.array(np.int32(line2))
#                 indeces = np.where(cleanLines > args.threshold) 
#                 if len(indeces[0]) == 0:
#                     pass
#                 elif len(indeces[0]) < 101:
#                     pass
#                 else:                    
#                     profVal = cleanLines[indeces[0]]
#                     seqPosFinal = seqPosPre[indeces[0]]
#                     for a,b in zip(seqPosFinal,profVal):
#                         s = '{} {}\n'.format(a,b)
#                         h.write(s)