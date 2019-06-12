#!/anaconda2/bin/python

# How to use:
# run this in directory containing group profiles (p0 etc)
# output should be all bed files
import os, argparse, csv, re, subprocess
import numpy as np
import linecache
from collections import Counter
from scipy.signal import find_peaks
from glob import glob

profileList = glob('*burnin.p*')
changePointFile = glob('*burnin.cp')[0]
filteredMAF = glob('filtered_*.maf')[0]
encodingFile = glob('chr*Encoded')[0]
for i in profileList:
	item = i
	print item
	outName = item.split('.')[0]+'_'+item.split('.')[2]+'.bed'
	command = ('gpToBed.py -gpFile {} -maf {} -cpFile {} '
		'-encoding {} -o {}').format(i,filteredMAF,changePointFile,
		encodingFile, outName)
	os.system(command)