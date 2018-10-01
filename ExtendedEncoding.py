#!/usr/bin/py
# This is just the conditional part of the encoding.
# There are 6 different indels I J K L M N depending on the combination of where the gaps are
import argparse
import os

parser = argparse.ArgumentParser()

#-i INPUTFILE -o OUTPUTFILE -c CHROMNUM
parser.add_argument("-i", "--inputfile", help = "input file")
parser.add_argument("-o", "--outputfile", help = "output file")
# parser.add_argument("-c", "--chromnum", help = "chomosome number")

args = parser.parse_args()

inputFile = args.inputfile
outputFile = args.outputfile

if os.path.isfile(outputFile) == False:
    pass
else:
    os.remove(outputFile)


# function to take an alignment block, encode it, then add a '# at the end'
def encoding(org1,org2,org3):
    outSeq = ''
    for c,d,e in zip(org1,org2,org3):
        if c == '-' and d == '-' and e =='-':
        	pass
    	elif c != '-' and d == '-' and e =='-':
    		outSeq += 'N'
    	elif c == '-' and d != '-' and e =='-':
    		outSeq += 'L'
    	elif c != '-' and d != '-' and e =='-':
    		outSeq += 'K'
    	elif c == '-' and d != '-' and e !='-':
    		outSeq += 'J'
    	elif c == '-' and d == '-' and e !='-':
    		outSeq += 'M'
    	elif c == '-' and d != '-' and e =='-':
    		outSeq += 'I'
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
    outSeq += '#'
    return outSeq


with open(inputFile) as foo:
        with open('temp', 'a+') as bar:
            countLine = 0
            for line in foo:

                if '##maf' in line:
                    pass #do nothing with header line
                
                if len(line) == 1:
                    pass #do nothing with empty lines

                if line[0] == 's':
                    # do things where the we have 's'pecies lines
                    # create a list where each of the entries are the bits of information in the .maf file

                    dirtyLine_1 = line.upper().split(' ')
                    org1 = list(filter(lambda thing: thing != '', dirtyLine_1))
                    org1_seq = org1[6] #this is just where the sequence part lives after filtering
                    
                    #same for species 2
                    dirtyLine_2 = foo.next().upper().split(' ')
                    org2 = list(filter(lambda thing: thing != '', dirtyLine_2))
                    org2_seq = org2[6]

                    #same for species 3
                    dirtyLine_3 = foo.next().upper().split(' ')
                    org3 = list(filter(lambda thing: thing != '', dirtyLine_3))
                    org3_seq = org3[6]
                    
                    # do encoding
                    encodedBlock = encoding(org1_seq,org2_seq,org3_seq)

                    # write to temp file
                    bar.write(encodedBlock)



with open("temp","r") as coo:
    with open(outputFile,"a+") as g:
        variable = coo.readline()
        variable = variable[:-1]
        g.write(variable)
    
os.remove("temp")















