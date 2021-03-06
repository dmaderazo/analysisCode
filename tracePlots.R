# This script generates traceplots of parameters given log files
# in the directory where this is run
rm(list = ls())
library(ggplot2)
library(reshape2)
library(dplyr)
# Input the file you care about
system('mkdir logPlots')
# Read in the header
allFiles <- system('ls *.log', intern = TRUE)
for (foo in allFiles){
  fileName <- foo
  
  #create subdirectory to save plots to 
  subDir <- paste0('subdir',foo)
  system(sprintf('mkdir %s', subDir))
  
  command1 <- sprintf("head -n 1 %s > tempFile", fileName)
  system(command1)
  
  cPointCommand <- read.table(file = 'tempFile', header = FALSE)
  cPointCommand <- t(cPointCommand)
  ## ~~~~~~ Warning! ~~~~~~
  ## Think about what happens in the case where a chain
  ## is continued on. This changes the number of lines 
  ## in the header.
  # catch strings
  flags <- c("-n", "-ng")
  # Process header to retrieve numSims and numGp:
  for (i in 1:length(cPointCommand)){
    if (cPointCommand[i] == "-n"){
      numSims <- cPointCommand[i+1]
      numSims <- as.integer(numSims)
    } else if (cPointCommand[i] == "-ng") {
      
      numGp <- cPointCommand[i+1]
      numGp <- as.integer(numGp)
    }
  }
  
  command2 <- sprintf("head -n 4 %s | tail -n 1 > rTemp.r", fileName)
  system(command2)
  source('rTemp.r')
  # alphsize
  system('rm -rf tempFile')
  system('rm -rf rTemp.r')
  # Read in the 'juicy' part of the .log file from n = 8, 
  # header = FALSE
  # nrows = numSamples
  # Be careful about that pesky final entry
  command3 <- sprintf("grep -n 'Beginning MCMC' %s | grep -Eo '^[^:]+'", fileName)
  startLine <- system(command3, intern = TRUE)
  df <- read.table(fileName, header = FALSE, nrows = numSims, sep = " ", skip = startLine)
  
  # Process the data frame
  # Drop first colum (only contains indecies)
  df <- df[-1]
  
  # Drop the last column
  df <- df[-length(df)]
  # name the columns
  var1 <- "numCP"
  
  mixProps <- sprintf("mixProp%02d", 0:(numGp-1))
  
  alphas <- rep(sprintf("alphaGp%02d_",0:(numGp-1)), alphsize)
  
  alphas <- matrix(alphas, nrow = alphsize, byrow = TRUE)
  
  alphabetChar <- sprintf("%02d",0:(alphsize-1))
  
  for (i in 1:numGp){
    alphas[,i] <- paste0(alphas[,i],alphabetChar)
  }
  
  temp <- c(alphas)
  
  lnLike <- "logLikelihood"
  
  headers <- c(var1, mixProps, temp, lnLike)
  
  colnames(df) <- headers
  # The mixture proportions will be given by the
  # next ng entries.
  
  # plots
  iterSeq <- seq(1:numSims)
  
  ggplot(data = df, aes(x = seq(1:numSims), y = numCP, group = 1)) + 
    geom_line() + xlab('Iteration') + ylab('Number of change points') + 
    ggtitle(sprintf('NumCp, ng=%s',numGp)) + theme_minimal()
  ggsave('NumCp.pdf', plot = last_plot(), path = subDir)
  # df[,2] to df[,2+(numGp-1)] will be the mx Props
  mixPropdf <- df[grep('mixProp', colnames(df))]
  # mixPropMeans <- colMeans(mixPropdf)
  # write.table(mixPropMeans, file = paste(fileName,'MixPropMeans.txt',sep = ''))
  
  mixPropdf$iter <- iterSeq
  mixPropdf <- melt(mixPropdf, id.vars = 'iter')
  
  ggplot(mixPropdf, aes(x = iter, y = value, colour = variable)) + 
    geom_line() + xlab('Iteration') + ylab('Mixture Proportions') +
    ggtitle(sprintf('Mixture proportions Time Series, ng=%s', numGp)) + theme_minimal()
  ggsave('MixProps.pdf', plot = last_plot(), path = subDir)
  
  gpIndex = sprintf('%02d_',0:(numGp-1))
  for (i in gpIndex){
    gpDf <- df[grep(sprintf('alphaGp%s',i), colnames(df))]
    gpDf$iter <- iterSeq
    gpDf <- melt(gpDf, id.vars = 'iter')
    
    ggplot(gpDf, aes(x = iter, y = value, colour = variable)) +
      geom_line() + xlab('Iteration') + ylab('Param Value') + 
      ggtitle(sprintf('Pram Time Series, ng=%s', numGp)) + theme_minimal() +
      theme(legend.position = "none")
    ggsave(sprintf('%sGp.pdf',i), plot = last_plot(), path = subDir)
  }
  
  ggplot(data = df, aes(x = iterSeq, y = logLikelihood)) +
    geom_line() + xlab('Iteration') + ylab('Log Likelihood') + 
    ggtitle(sprintf('Ln Likelihood Time Series, ng=%s',numGp)) + theme_minimal()
  
  logPlotName <- sprintf("LogLikelihood_%02d.pdf", as.numeric(numGp))
  ggsave(logPlotName, plot = last_plot(), path = subDir)
  moveLogPlot <- sprintf('cp ./%s/%s ./logPlots',subDir,logPlotName)
  system(moveLogPlot)
}

system('mkdir logPlotDirs')
system('mv subdir* ./logPlotDirs')

rm(list = ls())

system('getLnDataframe.py -o myDF')