#!/bin/bash
#
# Script to illustrate running batch jobs and passing in arguments.
#
# 
# This script assumes that the following has been run successfully:
# scons co=1 b=GccOpt ts=projects/TanCollaboration/test/TestCryptInvasion.hpp
#
cd ../../../
initial_sim=2;
offset=0;
num_runs=1;
num_sweeps=10; #This number of sims starting from $initial_sim
for (( i=0 ; i<${num_sweeps} ; i++))
do
    temp_num=`expr $i \* $num_runs + $initial_sim`;
    #offset_num_runs=`expr $num_runs-$offset`;

    if [  $temp_num -lt 10 ]
    then
    	pad="0"
    	sim_num="$pad$temp_num"
    else
    	sim_num=$temp_num
    fi

    echo $sim_num

    #nice -20 changePoint -i chr1Encoded  -n 1000 -b 1000 -s 100000 -ng  sim_num -o seg_ng_$sim_num > ./outMessages/stdoutseg_ng_$sim_num.txt & 
 
done

echo "Jobs submitted"

