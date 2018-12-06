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

for (( i=0 ; i<${num_sweeps} ; i++))
do
    start_sim=`expr $i \* $num_runs + $initial_sim`;
    #offset_num_runs=`expr $num_runs-$offset`;
    echo $start_sim
        # NB "nice -20" gives the jobs low priority (good if they are going to dominate the server and no slower if nothing else is going on)
        # ">" directs std::cout to the file.
        # "2>&1" directs std::cerr to the same place.
        # "&" on the end lets the script carry on and not wait until this has finished.
        # nice -20 projects/TanCollaboration/build/optimised/TestCryptInvasionRunner -run_index $start_sim -num_runs $offset_num_runs -is_tan true -is_gamma_1 true   > projects/TanCollaboration/test/output/TanCryptInvasionRun_${i}_Output.txt 2>&1 &
        # nice -20 projects/TanCollaboration/build/optimised/TestCryptInvasionRunner -run_index $start_sim -num_runs $offset_num_runs -is_tan false  -is_gamma_1 true > projects/TanCollaboration/test/output/VL1CryptInvasionRun_${i}_Output.txt 2>&1 &
        #nice -20 projects/TanCollaboration/build/optimised/TestCryptInvasionRunner -run_index $start_sim -num_runs $offset_num_runs -is_tan false  -is_gamma_1 false > projects/TanCollaboration/test/output/VL2CryptInvasionRun_${i}_Output.txt 2>&1 &
        # nice -20 changePoint -i -o2>&1 &
    nice -20 changePoint -i chr1Encoded  -n 1000 -b 1000 -s 100000 -ng $start_sim -o seg_ng_$start_sim > ./outMessages/stdoutseg_ng_$start_sim.txt & 
 
done

echo "Jobs submitted"


