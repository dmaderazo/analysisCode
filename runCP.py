#!/usr/bin/python
#This script should run CP for a range of segmenr groups
#Default Parameters:	
#	-n = 1000
#	-b = 500
# 	-s = 1000 (need to tune this per problem)
#	- 

import os
import argparse

parser = argparse.ArgumentParser()

#Import stuff
parser.add_argument('-n','--num_samples',help='number of samples int >= 1 default = 1000',type=str,
	default='1000')
parser.add_argument('-b','--num_burn',help='burn in, default = 500',type=str,
	default='500')
parser.add_argument('-s','--sample_block',help='sampling block size, this should be tuned per problem',type=str,
	default='1000')
parser.add_argument('-i','--input_file',help='Coded Alignment',type=str)
parser.add_argument('-o','--ouptut_file',help='ouptut_file name',type=str)
parser.add_argument('-sf','--seg_file',help='.log file to continute segmentation',type=str,
	default='')
parser.add_argument('-r','--num_range',help='range of groups to trym default = 20',type=int,
	default='20')


args=parser.parse_args()

for i in range(2, args.num_range+1):
	# tempVar = 'bladh '+ str(i) +' more stuff'
	# print(tempVar)
	# from subprocess 
	# print(args.input_file)
	# print(args.ouptut_file)
	# print(args.sample_block)

	command_string=('ChangePoint -i '+args.input_file+ ' -o ' + args.ouptut_file + ' -n '+ args.num_samples+ ' -b ' + args.num_burn + ' -s ' + args.sample_block + ' -ng ' + str(i) + ' -sf ' + args.seg_file)

	# test_string='ls'

	os.system(command_string)




# print(args.num_samples)