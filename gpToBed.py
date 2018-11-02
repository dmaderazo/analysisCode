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
parser.add_argument("-maf", "--mafFile", help="filtered .maf alignment", type = str)
parser.add_argument("-t", "--threshold", help="Threshold", type = float, default=0.75)
# parser.add_argument("-chr","--chormosome", help = "Chromosome", type = str)
# parser.add_argument("-o", "--output", help='name of output file', type = str)
# parser.add_argument("-chr", "--chromosme", type = str)

args = parser.parse_args()
# chromNum = args.chr
# os.
segSize = 50 # Set this to be length of a seq in output file
# import pdb; pdb.set_trace()

if os.path.isfile('temp') == False:
    pass
else:
    os.remove('temp')

subprocess.call('touch temp',shell=True)

#         # for i in cleanLines

## Get Sequence positions. 
## Generate file that has sequence positions taken from .net.axt
## format:
## no. chrom_in_ref pos_start pos_end other_org pos_start pos_end seq_len

with open(args.mafFile) as f:
	with open('temp','w+') as g:
    # with open('tempFile', 'w+') as fleeb:
    # line = f.readlines()
	    for dirtyProfileLine in f:
	    	# print(lines)
	    	# print(len(lines))
	    	cleanProfileLine = dirtyProfileLine.split()

	    	if len(cleanProfileLine) <= 2:
	    		pass
	    	elif 'hg19'in cleanProfileLine[1]:
	    		seqLen = int(cleanProfileLine[3])
	    		if seqLen > segSize:
	    			q = seqLen/segSize
	    			r = seqLen % segSize
	    			# print r
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

gpFile = args.gpFile
with open('temp','r+') as yeet:
	with open(args.)
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