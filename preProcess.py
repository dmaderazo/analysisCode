#!/anaconda2/bin/python
import os 
import argparse
import csv
import pandas as pd
from collections import Counter
import glob
parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", help="galaxy_chrXXX.maf", type = str)

parser.add_argument("-o", "--output", type = str)

args = parser.parse_args()

temp  = args.input.split("_")[1]

chrom = temp.split('.')[0]

intermediate_name = chrom+'.maf'
command_1 = 'maf_parse -I -E {} > {}'.format(args.input,intermediate_name)

command_2 = 'ExtendedEncoding.py -i {} -o {}'.format(
	intermediate_name,args.output)

os.system(command_1)
os.system(command_2)