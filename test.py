# import os 
# import argparse
# import csv
# import re
# import numpy as np
# import subprocess

# parser = argparse.ArgumentParser()

# parser.add_argument('-y', '--this is an option', help='what',type = str )

# args = parser.parse_args


# print(args.y)

import argparse
import system
parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('-inFile', type=str, help='Input file for Change Point')
parser.add_argument('-n', type=int, help='a number')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# # parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

args = parser.parse_args()

# print(args.n)
# print(args.inFile)
os.print('this is a thing '%s,args.inFile)
# print(args.accumulate(args.integers))