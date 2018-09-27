#!/usr/bin/python

# Script to generate wiggle file
# Generate a wiggle track to identify segments that are:
#   >= 100 nt in length
#   Belong to class with >= 0.9 probability
#   Do I care about indels at this point? Probably not



# Dear me, please consider using proper code hygeine and writing actually informative comments.

import os 
import argparse
import csv
import re
import numpy as np
import subprocess
parser = argparse.ArgumentParser()

parser.add_argument("-gpfile", "--groupfile", help="group profile", type = str)
parser.add_argument("-axt", "--axtfile", help=".net.axt alignment", type = str)
parser.add_argument("-t", "--threshold", help="Threshold", type = float, default=0.9)
parser.add_argument("-o", "--output", help='name of output file', type = str)
# parser.add_argument("-chr", "--chromosme", type = str)

args = parser.parse_args()
# os.
# subprocess.call('touch tempFile',shell=True)
# import pdb; pdb.set_trace()



#         # for i in cleanLines

## Get Sequence positions. 
## Generate file that has sequence positions taken from .net.axt
## format:
## no. chrom_in_ref pos_start pos_end other_org pos_start pos_end seq_len

with open(args.axtfile) as f:
    with open('tempFile', 'w+') as fleeb:
    # line = f.readlines()
        for lines in f:
            firstLet = lines[0]
            if re.search('[0-9]',firstLet):
                # print(lines[0])
                # cleanLines = lines.split(' ')
                fleeb.write(lines)

# create file with sequence positions in ref organism (just numbers)
with open('tempFile','r') as thing:
    with open('thisTest','w+') as blah:
        for line in thing:
            axtLine = line.split()
            startNum = int(axtLine[2])
            endNum = int(axtLine[3])
            sequencePositions = range(startNum,endNum + 1)
            seqPos = ','.join(map(repr,sequencePositions))


            blah.write('{}\n'.format(seqPos))


#writes a wiggle track 
#format
#Seq_pos profile value (how to filter?)
with open('thisTest','r') as f:
    with open(args.groupfile, 'r') as g:
        with open(args.output,'w+') as h:
            gpData = csv.reader(g)
            seqPos = csv.reader(f)
            
            for line1,line2 in zip(gpData,seqPos):
                cleanLines = np.array(np.float_(line1[1:]))
                seqPosPre = np.array(np.int32(line2))
                indeces = np.where(cleanLines > args.threshold) 
                if len(indeces[0]) == 0:
                    pass
                elif len(indeces[0]) < 101:
                    pass
                else:                    
                    profVal = cleanLines[indeces[0]]
                    seqPosFinal = seqPosPre[indeces[0]]
                    for a,b in zip(seqPosFinal,profVal):
                        s = '{} {}\n'.format(a,b)
                        h.write(s)