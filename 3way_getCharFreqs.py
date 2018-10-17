from __future__ import division
# ## Python function/script to estimate character frequencies 
# Given a .cp, profile file and encoding, estimate the character frequences in a class
# Approach:
#     Read in group profile and then set a threshold. 
#     Consider all positions that are above the threshold to be part of the group
# 
#     Get corresponding position in the alignment encoding and count the frequency
# 
#     output summary

import os 
import argparse
import csv

parser = argparse.ArgumentParser()

#-db DATABSE -u USERNAME -p PASSWORD -size 20
parser.add_argument("-gpfile", "--groupfile", help="group profile", type = str)
parser.add_argument("-i", "--input", help="Coded alignment", type = str)
parser.add_argument("-t", "--threshold", help="Threshold", type = float)
parser.add_argument("-o", "--output", type = str)


args = parser.parse_args()

print( args.groupfile )

with open(args.input) as f:
    lines = f.readlines()
    lines = lines[0].split('#')

rowIndex = 0

with open(args.groupfile, 'r') as f:
    with open(args.output,'w') as g:
            
        myFile = csv.reader(f)
        for line in myFile:        
            clean_line = line[1:]
            for i in range(0,len(clean_line)-1):
                value = float(clean_line[i])

                if value > args.threshold:
                    char = lines[rowIndex][i]
                    g.write(char)
            rowIndex = rowIndex + 1   

with open(args.output,'r') as g:
    s = g.read()
    consProp = s.count('a') + s.count('v')
    consProp = consProp/len(s)
    print "The frequency of a is {}".format(s.count('a')/len(s))
    print "The frequency of v is {}".format(s.count('v')/len(s))
    print "Conservation proportion is {}".format(consProp)
    print "The number of sequence positions with > {} probability of being in this class is {}".format(args.threshold, len(s))