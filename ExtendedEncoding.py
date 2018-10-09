#!/usr/bin/py
# This is just the conditional part of the encoding.
# There are 6 different indels I J K L M N depending on the combination of where the gaps are
import argparse
import os
import subprocess

# function to identify proportion of string made up of elements of bad letters 
def char_prop(word):
    # THIS IS CASE SENSITIVE
    badSet = {'I','J','K','L','M','N','#'}
    word_len = float(len(word))
    char_count = 0

    for c in word:
        if c in badSet:
            char_count += 1

    return (char_count/word_len) 
# function to count lines of input file
# def file_len(fname):
#     p = subprocess.Popen(['wc', '-l', fname], stdout=subprocess.PIPE, 
#                                               stderr=subprocess.PIPE)
#     result, err = p.communicate()
#     if p.returncode != 0:
#         raise IOError(err)
#     return int(result.strip().split()[0])
# function to take an alignment block
def encoding(org1,org2,org3):
    #Define our bad letters
    badSet = {'I','J','K','L','M','N'}
   
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
    # outSeq += '#'    

    # find the set of letters in outSeq
    wordSet = set(outSeq)

    #if the word is made up entirely of bad characters discard 
    if wordSet <= badSet:
        return None
    #This is necessary for change point input.

    # if the word is too short discard
    ## ASK JON ABOUT THIS. Do I do this before or after?
    elif len(outSeq) < 7:
       return None
    # if the word is made up of mostly gaps, discard
    #elif char_prop(outSeq) > 0.5:
     #   return None
    else: #return outSeq
        return outSeq


parser = argparse.ArgumentParser()

#-i INPUTFILE -o OUTPUTFILE -c CHROMNUM
parser.add_argument("-i", "--inputfile", help = "input file")
parser.add_argument("-o", "--outputfile", help = "output file")

args = parser.parse_args()

inputFile = args.inputfile
outputFile = args.outputfile
newBed = 'filtered_'+inputFile

# lineCount = file_len(inputFile)

# delete any file that has the same name as the output 
if os.path.isfile(outputFile) == False:
    pass
else:
    os.remove(outputFile)

# delete any file that has the same name as the filtered maf
if os.path.isfile(newBed) == False:
    pass
else:
    os.remove(newBed)

with open(inputFile) as foo:
        with open(outputFile, 'a+') as bar:
            with open(newBed,'a+') as foobar:
                foobar.write('##maf version=1')   
                foobar.write('\n') 
                isFirstPass = 1

                for line in foo:

                    if '##maf' in line:
                        # foobar.write(line) #write header line
                        pass
                    
                    if len(line) == 1:
                        pass #do nothing with empty lines

                    if line[0] == 'a': #store the score lines
                         aLine = line

                    if line[0] == 's':
                        # do things where the we have 's'pecies lines
                        # create a list where each of the entries are the bits of information in the .maf file

                        pre_dirt_1 = line
                        dirtyLine_1 = pre_dirt_1.upper().split(' ')
                        org1 = list(filter(lambda thing: thing != '', dirtyLine_1))
                        org1_seq = org1[6] #this is just where the sequence part lives after filtering
                        
                        #same for species 2
                        pre_dirt_2 = foo.next()
                        dirtyLine_2 = pre_dirt_2.upper().split(' ')
                        org2 = list(filter(lambda thing: thing != '', dirtyLine_2))
                        org2_seq = org2[6]

                        #same for species 3
                        pre_dirt_3 = foo.next()
                        dirtyLine_3 = pre_dirt_3.upper().split(' ')
                        org3 = list(filter(lambda thing: thing != '', dirtyLine_3))
                        org3_seq = org3[6]
                        
                        # do encoding
                        encodedBlock = encoding(org1_seq,org2_seq,org3_seq)
                        # write to file if we care about the block
                        if encodedBlock != None:
                            foobar.write(aLine)
                            foobar.write(pre_dirt_1)
                            foobar.write(pre_dirt_2)
                            foobar.write(pre_dirt_3)
                            foobar.write('\n')
                        # while countLine < lineCount:
                        #     encodedBlock += '#'
                        # write to temp file
                        if encodedBlock == None:
                            pass
                        elif isFirstPass == 1:
                            bar.write(encodedBlock)
                            isFirstPass = 0
                        elif isFirstPass != 1:
                            bar.write('#'+encodedBlock)


# can remove this now. 

# with open("temp","r") as coo:
#     with open(outputFile,"a+") as g:
#         variable = coo.readline()
#         variable = variable[:-1] #remove the last '#' because ChangePoint will freak out otherwise
#         g.write(variable)
    
# os.remove("temp")
