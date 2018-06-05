#!/bin/bash

rm -rf tempFile

for i in *.log
do 
  	logRetriever.sh -a $i
done  > tempFile

#pick a file

fileName=$(ls *.log | head -n 1)

#count the number of lines in that file

lineCount=$(wc -l < $fileName)

#return the number of lines less the current header (-9)
#plus the file name header (+1)
# this is the no. of rows for output
lineCount="$(($lineCount-9+1))" 


#number of columns is the number of files included
numCols=$(ls -l *.log | wc -l)
numCols="$(($numCols+0))" 

# wc -l < tempFile
#echo $lineCount
#echo $numCols

pr -ts"," -l$lineCount -$numCols tempFile 
	

