#!/usr/bin/python

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
#replace = "cat %s | tr '#' \\n > tempFile" % args.input
# replace = "cat {} | tr '#' \\n > tempFile".format(args.input)
# os.system(replace) # generates the file for looking at characters by block

# import subprocess
# new_replace = "cat {} | tr '#' \\n".format(args.input)
# import pdb; pdb.set_trace(); 
# p = subprocess.Popen(new_replace, stdout=subprocess.PIPE)
# output = p.communicate()
# with open("demo.txt", "w+") as f:
#     f.write(output.replace(" "*6,"\n"))
rowIndex = 0

with open(args.groupfile, 'r') as foo:
    with open(args.output,'w') as alice:
            
        myFile = csv.reader(foo)
        for line in myFile:        
            clean_line = line[1:]
            for i in range(0,len(clean_line)-1):
                value = float(clean_line[i])

                if value > args.threshold:
                    char = lines[rowIndex][i]
                    alice.write(char)
            rowIndex = rowIndex + 1    

with open(args.output,'r') as g:
    s = g.read()
    consProp = s.count('a') + s.count('f') + s.count('k') + s.count('p') 
    consProp = consProp/len(s)
    print "The frequency of a is {}".format(s.count('a')/len(s))
    print "The frequency of f is {}".format(s.count('f')/len(s))
    print "The frequency of k is {}".format(s.count('k')/len(s))
    print "The frequency of p is {}".format(s.count('p')/len(s))
    print "Conservation proportion is {}".format(consProp)
    print "The number of sequence positions with > {} probability of being in this class is {}".format(args.threshold, len(s))

                
