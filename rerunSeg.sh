#!/bin/bash

initial_sim=2;
offset=0;
num_runs=1;
num_sweeps=10; #This number of sims starting from $initial_sim
final_sim=20;

#### Parameters for changePoint ####
encodedFile=noExonsEncoded.txt
numIts=1000
numBurn=500
numSkip=100000

for sim_num in $(seq -w $initial_sim $final_sim);
do
	echo $sim_num
    # echo $sim_num > ./outMessages/stdoutseg_ng_$sim_num.txt 2>&1 &
    nice -20 changePoint -i $encodedFile  -sf seg_ng_$sim_num -n $numIts -b $numBurn -s $numSkip -ng  $sim_num -o rerun_ng_$sim_num > ./outMessages/stdoutrerun_ng_$sim_num.txt 2>&1 &
done
echo "Jobs submitted"