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