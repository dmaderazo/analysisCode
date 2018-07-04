# Script to generate wiggle file
# Generate a wiggle track to identify segments that are:
#   >= 100 nt in length
#   Belong to class with >= 0.9 probability
#   Do I care about indels at this point? Probably not

import os 
import argparse
import csv
import re
import numpy as np
import subprocess
parser = argparse.ArgumentParser()

parser.add_argument("-gpfile", "--groupfile", help="group profile", type = str)
parser.add_argument("-axt", "--axtfile", help=".net.axt alignment", type = str)
# parser.add_argument("-t", "--threshold", help="Threshold", type = float)
parser.add_argument("-o", "--output", type = str)
# parser.add_argument("-chr", "--chromosme", type = str)

args = parser.parse_args()
# os.
# subprocess.call('touch tempFile',shell=True)
# import pdb; pdb.set_trace()



#         # for i in cleanLines

## Get Sequence positions. 
with open(args.axtfile) as f:
    with open('tempFile', 'w+') as fleeb:
    # line = f.readlines()
        for lines in f:
            firstLet = lines[0]
            if re.search('[0-9]',firstLet):
                # print(lines[0])
                # cleanLines = lines.split(' ')
                fleeb.write(lines)
                # startNum = int(cleanLines[2])
                # endNum = int(cleanLines[3])
                # range(startNum,endNum))
    #     #print(lines[0])
    #     if lines[0] != (_[A-Za-z]_ or '#'):
    #         print('trigger')
with open('tempFile','r') as thing:
    with open('thisTest','w+') as blah:
        for line in thing:
            axtLine = line.split()
            startNum = int(axtLine[2])
            endNum = int(axtLine[3])
            sequencePositions = range(startNum,endNum + 1)
            seqPos = ','.join(map(repr,sequencePositions))
            blah.write('{}\n'.format(seqPos))

with open('thisTest','r') as f:
    with open(args.groupfile, 'r') as g:
        with open(args.output,'w+') as h:
            gpData = csv.reader(g)
            seqPos = csv.reader(f)
            
            for line1,line2 in zip(gpData,seqPos):
                cleanLines = np.array(np.float_(line1[1:]))
                seqPosPre = np.array(np.int32(line2))
                indeces = np.where(cleanLines > 0.9)
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

# import pdb; pdb.set_trace()
# Make a file that contains long sequence positions
# with open('tempFile2','w+') as f:
#     with open(args.groupfile) as g:
#         myFile = csv.reader(g)
#         # import pdb; pdb.set_trace()
#         for line1 in f:
#             print line1
#             # import pdb; pdb.set_trace()
 
# with open(args.groupfile) as foo:
#     with open('tempFile') as fp:
#         myFile = csv.reader(foo)
#         # import pdb; pdb.set_trace()
#         lineCount = 0
#         # fp = open('tempFile')
#         pf = open('posFile','a+')
#         for line in myFile:
#             # import pdb; pdb.set_trace()
#             cleanLines = np.array(np.float_(line[1:]))
#             indeces = np.where(cleanLines > 0.9)
#             print len(indeces[0])
#             if len(indeces[0]) == 0:
#                 pass
#             else:
#                 pVlaue = cleanLines[indeces[0]]
                
#                 for i, blah in enumerate(fp):
#                     # print 'fuck, this is {}'.format(i)
#                     # print indeces
#                     # print 'lineCount = {}'.format(lineCount)
#                     if i == lineCount:
#                         axtLine = blah.split()
#                         startNum = int(axtLine[2])
#                         endNum = int(axtLine[3])
#                         numbers = np.array(range(startNum,endNum+1))
#                         # print(len(indeces[0]))
#                         # print(indeces[0])
#                         # print 'line No.{}'.format(i)
#                         seqPos = numbers[indeces[0]]
#                         # import pdb; pdb.set_trace()
#                         # numbers = ','.join(map(repr,numbers.tolist()))
#                         pf.write(','.join(map(repr,seqPos.tolist())))
#                         print 'hello it is iteration {}'.format(i)
                        
#                     # else:
#                     #     break
#                     # i=i+1
#             lineCount = lineCount + 1
#             print 'the line count is {}'.format(lineCount)
#         print 'you are here'
            
        # fp.close()
        # pf.close()
