## This is a piece of code to do an ecoding between two species 
## I think it could be faster.


import argparse
parser = argparse.ArgumentParser()

#-i INPUTFILE -o OUTPUTFILE -c CHROMNUM
parser.add_argument("-i", "--inputfile", help = "input file")
parser.add_argument("-o", "--outputfile", help = "output file")
parser.add_argument("-c", "--chromnum", help = "chomosome number")

args = parser.parse_args()
# files of interest



inputFile = args.inputfile
outputFile = args.outputfile

import os 
if os.path.isfile(outputFile) == False:
    pass
else:
    os.remove(outputFile)
    
# set this to be the chromosome
chroNum = args.chromnum.lower()

# A collection of conditional statements that
# does the encoding for TWO species in a .net.axt alignment
#import numpy

def encoding(org1,org2):
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



with open(inputFile) as foo:
    with open("temp", "a+") as bar:

        for line in foo:
            # if line in ['\n', '\r\n']:
            #     print("the Next line is empty")

            if chroNum in line.lower():
            
                refOrg = foo.next().upper()
                queryOrg = foo.next().upper()
   
                testOut = encoding(refOrg,queryOrg)

                bar.write(testOut)
# Sliding Window Python 
#itertools
        
with open("temp","r") as coo:
    with open(outputFile,"a+") as g:
        variable = coo.readline()
        variable = variable[:-1]
        g.write(variable)
    
os.remove("temp")
        
# with open(outputFile,"a+") as bar:
#     encSeq = bar.readline()
#     print(encSeq)
#     encSeq = encSeq[:-1]
#     print(encSeq)
#     bar.write(encSeq)



     