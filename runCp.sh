#!/bin/bash

## This script runs changePoint for a number of segment classes. (Hard coded 2 to 20)
## input file name is hard coded

nums=$(seq -w 2 20)

for i in $nums
do
	changePoint -i INPUTFILENAME -o OUTPUFILENAMEng$i -n 1000 -ng $i -s 10000	
done

