

# input should be .maf. This changes the strand on ALL species to "+"

import os, argparse, csv, re, subprocess
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-maf", "--mafFile", help="filtered .maf alignment", type = str)

args = parser.parse_args()

mafFile = args.mafFile
output = 'pm_'+mafFile
with open(mafFile,'r') as f:
	with open(output,'w+') as g:
		for line in f:
			whole_line = line.split()
			if len(whole_line) > 0:
				if whole_line[0] == 's':
					whole_line[4] = '+'
				writeString = ' '.join(whole_line)+'\n'
			else:
				writeString = '\n'
			g.write(writeString)

