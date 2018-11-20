# Function to assess whether or not regions identified in a .bed file 
# are partially/completely contained or close to another region in a 
# different .bed file

# input:

# 	queryFile
# 	referenceFile

# 	(both should be .bed format)

import os, argparse, csv, re, subprocess
import numpy as np
parser = argparse.ArgumentParser()

parser.add_argument("-qFile","--queryFile")
parser.add_argument("-rFile","referenceFile")

args=parser.parse_args()

qFile = args.queryFile
rFile = args.referenceFile


def myfun(qFile,rFile):
	for line in 

# do a thing with np.c_[] to stack 1D arrays into column wise 
np.savetxt(fileName, ARRAY ,fmt=%d, delimiter=',')