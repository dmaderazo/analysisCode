#!/usr/bin/python
# Filter .maf file for only chromNum
# This is just the conditional part of the encoding.
# There are 6 different indels I J K L M N depending on the combination of where the gaps are
import argparse
import os
import subprocess

#filter out maf files to include only the blocks with the things that we want


parser = argparse.ArgumentParser()

#-i INPUTFILE -o OUTPUTFILE -c CHROMNUM
parser.add_argument("-i", "--inputfile", help = "input file")
parser.add_argument("-o", "--outputfile", help = "output file")
parser.add_argument("-c","--chromnum",help = "chromosome of interest",type = str)

args = parser.parse_args()

chromnum = args.chromnum
inputFile = args.inputfile
outputFile = args.outputfile
newBed = 'filtered_'+inputFile+'_'+chromnum #Should be MAF

filterKey = 'danRer7.'+chromnum
filterKey = filterKey.upper()
print(filterKey)
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
                    
                  
                    # write to file if we care about the block
                    if org1[1] == filterKey:
                        foobar.write(aLine)
                        foobar.write(pre_dirt_1)
                        foobar.write(pre_dirt_2)
                        foobar.write(pre_dirt_3)
                        foobar.write('\n')


