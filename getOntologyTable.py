# bang and stuff

# should be run in direcotry with cluster_tsv files
# iterates over all tsv files and determines what ontologies are present
# YOU SHOULD SET THE NUMBER OF CLUSTERS

from glob import glob
from collections import OrderedDict
from collections import Counter 
import pandas as pd 

print 'MAKE SURE YOU HAVE SET THE NUMBER OF CLUSTERS'
numClust = 17

fileList = glob('*cluster_*.tsv')
ontoList = (['GO Biological Process','GO Cellular Component',
	'GO Molecular Function','Human Phenotype','Mouse Phenotype Single KO',
	'Mouse Phenotype'])


clusterNums = ([int(fileList[i].split('.')[0].split('_')[-1]) 
	for i in range(len(fileList))])

# set of clusters that don't have a tsv
noTsv = set.difference(set(range(1,numClust+1)),set(clusterNums))

#init dictionary
clustNames = (['Cluster {}'.format(i) for i in range(1,numClust+1)])
colNames = ['Ontologies'] + clustNames
myDict = OrderedDict.fromkeys(colNames)
myDict['Ontologies'] = ontoList
#populate empty keys
for i in noTsv:
	emptyKey = 'Cluster {}'.format(i)
	myDict[emptyKey] = [0]*len(ontoList) #['\\xmark']*len(ontoList)
#populate non empty keys
for i in fileList:
	clustId = int(i.split('.')[0].split('_')[-1])
	keyName = 'Cluster {}'.format(clustId)
	# read ontologies column only
	df = pd.read_csv(i,header=None,usecols=[0],skiprows = [0,1],sep='\t')
	# convert to set 
	presentOntologies = set(df.loc[:,0])

	# empty dict to be populated with ticks and crosses
	ontoDict = OrderedDict.fromkeys(ontoList)

	#present ontologies get a tick, the rest get a cross
	# for j in ontoList:
	# 	if j in presentOntologies:
	# 		ontoDict[j] = '\\cmark'
	# 	else: 
	# 		ontoDict[j] = '\\xmark'
	# lets count them instead
	ontoCounts = Counter(df[0])
	for j in ontoList:
		if j in presentOntologies:
			ontoDict[j] = 1 #ontoCounts[j]
		else: 
			ontoDict[j] = 0

	myDict[keyName] = ontoDict.values()


tempDf = pd.DataFrame.from_dict(myDict)


# tempDf = tempDf[['Ontologies','Cluster 14','Cluster 10','Cluster 15','Cluster 6','Cluster 2','Cluster 17','Cluster 5','Cluster 9','Cluster 8','Cluster 11','Cluster 1','Cluster 16','Cluster 13','Cluster 4','Cluster 7','Cluster 3','Cluster 12']]

# delet
#blah = ['Cluster 14','Cluster 10','Cluster 15','Cluster 6','Cluster 2','Cluster 17','Cluster 5','Cluster 9','Cluster 8','Cluster 11','Cluster 1','Cluster 16','Cluster 13','Cluster 4','Cluster 7','Cluster 3','Cluster 12']
#tempNames = [i.split(' ')[-1] for i in blah]
transDf = tempDf.T
transDf.to_csv('binaryOutFrame.csv',header=True)
# import pdb; pdb.set_trace()
# tempDf.columns(tempNames)
tempDf.to_csv('binaryDendoOutFrame.csv',index = False)




