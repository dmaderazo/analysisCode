from glob import glob
import os

fileList = glob('*.csv')

for i in fileList:
	groupNum = i.split('.')[0].split('_')[-1]
	outName = groupNum+'_'+'bestClass.txt'
	estimateName = groupNum+'_estimates.txt'

	command = 'Rscript ./combiningScript.R {} {} {}'.format(i,outName,estimateName)
