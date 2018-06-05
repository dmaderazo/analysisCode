#!/bin/bash

#nums=$(seq 1 3)

#for i in $nums
#do
#	touch file$i
#done

i=0

while [ $i -lt 4 ]
do 
	echo $i
	i=`expr $i + 1`
done

