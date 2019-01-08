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
num_sweeps=10;
final_sim=20;

for start_sim in $(seq -w $initial_sim $final_sim);
do
    start_sim=`expr $i \* $num_runs + $initial_sim`;
    #offset_num_runs=`expr $num_runs-$offset`;
    echo $start_sim
    nice -20 changePoint -i chr1Encoded  -n 1000 -b 1000 -s 100000 -ng $start_sim -o seg_ng_$start_sim > ./outMessages/stdoutseg_ng_$start_sim.txt & 
 
done

echo "Jobs submitted"


