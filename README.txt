> Processing.R 
	Run this in the directory where .log files are downloaded. 
	It will create subdirectories for every .log file and will plot:
		The number of change points
		The mixture proportions of the groups
		The Alphas for each group
		The Loglikelihood

> BasicEncoding.py 
	This script will take the following arguments
		-i input file: The input axt.net file required to be aligned
		-o output file: Name for output
		-c chromnum: The chromosome number of the reference organism
	A 16 characted encoding is create, see Keith papers for details

> datecp 
	Tells the date and time

> runcp.sh 
	Runs changepoint for a range of segment classes ( currently hard coded 2 to 20 )

> getLogLikelihood.sh
	Iterates over all the .log files in the directory and extracts the 
	log likelihoods over each iteration

> logRetreiver.sh
	Needs to be in the same directory so that getLogLikelihood will work.
	
> getCharFreqs.py
	Takes the following arguments
		-i input: Coded alignment
		-o output
		-t threshold: the minimum value to take a seq position into account
		-gpfile: profiled group file
	Calculates the Conservation of the group by looking at sequence
	positions that are greater than threshold value

		
