#!/bin/bash
#
# Script to illustrate running batch jobs and passing in arguments.
#
# 
# This script assumes that the following has been run successfully:
# scons co=1 b=GccOpt ts=projects/TanCollaboration/test/TestCryptInvasion.hpp
#
#cd ../../../
mkdir modelTest
initial_sim=2;
offset=0;
num_runs=1;
num_sweeps=10; #This number of sims starting from $initial_sim
final_sim=20;

#### Parameters for changePoint ####
encodedFile=chr6Encoded
numIts=1000
numBurn=0
numSkip=1000
num_groups=16
num_groups_less_run=$num_groups-1
# To correctly use this program, you must have the following parameters:
#   -i change-point_input_file_name
#   -c change_point_output_file_name1 ... (up to 150 file names)
#   -b num_burn (optional, default 0)
#   -s num_skip (optional, default 0)
#   -ng num_groups (optional, default 2)
#   -pg list of profiled group numbers (optional, default ng-1)
#   -notheta suppress theta profile (optional)
#   -nop suppress p profile (optional)



for group_num in $(seq -w 0 `expr $num_groups - 1`);
do
    echo $group_num
    # echo $sim_num > ./outMessages/stdoutseg_ng_$sim_num.txt 2>&1 &
    nice -20 readcp -i $encodedFile  -c chr6_ng_16  -b $numBurn -ng  $num_groups -pg $group_num > ./modelTest/readcpout_$group_num.txt 2>&1 &
done
echo "Jobs submitted"

