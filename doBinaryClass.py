import functions as fn 
import os 
import argparse
import csv
import pandas as pd
from collections import Counter
import glob

parser = argparse.ArgumentParser()

parser.add_argument('-i','--input',help='sorted group file in .bed format')
parser.add_argument('-o','--output',help='name of output .csv file')

args = parser.parse_args()
inputFile = args.input
outputFile = args.output
queryList=glob.glob('sorted_*')

isFirst = True

if os.path.isfile('temp.csv'):
	os.remove('temp.csv')

for queryFile in queryList:
	df_data=fn.classification(inputFile,queryFile,0.5)
	
	if isFirst:
		df_data.to_csv('temp.csv',index=False,header=True)
		isFirst=False
	else:
		storageDf=pd.read_csv('temp.csv',header=0)
		newDf=pd.concat([storageDf,df_data],axis=1)
		newDf.to_csv('temp.csv',index=False,header=True)

final_df = pd.read_csv('temp.csv',header=0)
final_df.to_csv(outputFile,index=False,header=True)

os.remove('temp.csv')





	



