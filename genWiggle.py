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
parser = argparse.ArgumentParser()

parser.add_argument("-gpfile", "--groupfile", help="group profile", type = str)
# parser.add_argument("-axt", "--axtfile", help=".net.axt alignment", type = str)
# parser.add_argument("-t", "--threshold", help="Threshold", type = float)
# parser.add_argument("-o", "--output", type = str)
# parser.add_argument("-chr", "--chromosme", type = str)

args = parser.parse_args()

# import pdb; pdb.set_trace()
with open(args.groupfile) as foo:
    myFile = csv.reader(foo)
    for line in myFile:
        import pdb; pdb.set_trace()
        cleanLines = np.array(np.float_(line[1:]))
        indeces = np.where(cleanLines > 0.9)
        if len(indeces[0]) == 0:
            pass
        else:
            cleanLines[indeces[0]]

        # for i in cleanLines

## Get Sequence positions. 
# with open(args.axtfile) as f:
#     # line = f.readlines()
#     for lines in f:
#         firstLet = lines[0]
#         if re.search('[0-9]',firstLet):
#             # print(lines[0])
#             cleanLines = lines.split(' ')
#             startNum = int(cleanLines[2])
#             endNum = int(cleanLines[3])
#             print(range(startNum,endNum))
#     #     #print(lines[0])
#     #     if lines[0] != (_[A-Za-z]_ or '#'):
#     #         print('trigger')


