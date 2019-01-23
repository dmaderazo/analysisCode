import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-o','--output',help='name of output .csv file')
args = parser.parse_args()
outputFile = args.output

if os.path.isfile('temp.csv'):
		os.remove('temp.csv')
	logFileList = glob.glob('*.log')
	isFirst = True

	for file in logFileList:
		
			with open(file) as foo:
				firstLine = foo.readline().split()
				numGroups = str(firstLine[firstLine.index('-ng')+1])
				numGroups_index = 'sim_'+numGroups
				numIts = float(firstLine[firstLine.index('-n')+1])

				# store these things into a df
				storageFrame = pd.DataFrame([numGroups_index,numGroups,numIts])

				# iterate through each line of the file to obtain lnLikelihood
				# print 'this is the start of the line loop'
				for line in foo:
					splitLine = line.split()
					lnLikelihoodValue = splitLine[-1]

					# print lnLikelihoodValue
					# print isfloat(lnLikelihoodValue)
					singleItemFrame = pd.DataFrame([lnLikelihoodValue])



					if isfloat(splitLine[0]):
						storageFrame = pd.concat([storageFrame,singleItemFrame],ignore_index=True)

						# print storageFrame

				if isFirst:
					storageFrame.to_csv('temp.csv',index=False,header=False) # Need to turn off option for row index and header
					isFirst = False
				else:
					data = pd.read_csv('temp.csv',header=None)
					data_df = pd.concat([data,storageFrame],sort=False,axis=1)
					data_df.to_csv('temp.csv',index=False,header=False)
	# read in new df
	final_df = pd.read_csv('temp.csv',header=0)

	final_df = final_df.reindex(sorted(final_df.columns),axis=1)

	final_df.to_csv(outputFile,index=False,header=True)
	os.remove('temp.csv')