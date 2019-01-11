#!/bin/bash
#
# Script to illustrate running batch jobs and passing in arguments.
#
# 
# This script assumes that the following has been run successfully:
# scons co=1 b=GccOpt ts=projects/TanCollaboration/test/TestCryptInvasion.hpp
#
#cd ../../../
mkdir outMessages
initial_sim=2;
offset=0;
num_runs=1;
num_sweeps=10; #This number of sims starting from $initial_sim
final_sim=20;

#### Parameters for changePoint ####
encodedFile=
numIts=1000
numBurn=1000
numSkip=1000

# for (( i=0 ; i<${num_sweeps} ; i++))
# do
#     temp_num=`expr $i \* $num_runs + $initial_sim`;
#     #offset_num_runs=`expr $num_runs-$offset`;

#     if [ $temp_num -lt 10 ]
#     then
#     	pad="0"
#     	sim_num="$pad$temp_num"
#     else
#     	sim_num=$temp_num
#     fi

#     echo $sim_num
#     # echo "test sim $sim_num" > ./outMessages/stdoutseg_ng_$sim_num.txt 2>&1 & 
#     nice -20 changePoint -i chr1Encoded  -n 1000 -b 1000 -s 100000 -ng  $sim_num -o seg_ng_$sim_num > ./outMessages/stdoutseg_ng_$sim_num.txt 2>&1 &
 
# done

for sim_num in $(seq -w $initial_sim $final_sim);
do
    echo $sim_num
    # echo $sim_num > ./outMessages/stdoutseg_ng_$sim_num.txt 2>&1 &
    nice -20 changePoint -i $encodedFile  -n $numIts -b $numBurn -s $numSkip -ng  $sim_num -o seg_ng_$sim_num > ./outMessages/stdoutseg_ng_$sim_num.txt 2>&1 &
done
echo "Jobs submitted"

