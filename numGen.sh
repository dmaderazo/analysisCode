#!/bin/bash

#pr -ts"," -l1001 -19 data.txt> prOut.txt

var=$(seq -w  1 100)

#echo $var

var2=$(ls -l cpOutng*.log | wc -l)
var1=$(wc -l )
#pr -ts"," -l$var1 -$var2 file > ThisThing.txt



