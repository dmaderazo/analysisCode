# Provides the DICVplot and mean MixProps for each model
rm(list = ls())
args = commandArgs(trailingOnly=TRUE)
library(ggplot2)
library(reshape2)
library(dplyr)

if (length(args)==0){
  numSamples = 1000
} else {
  numSamples = args
}

{
foo <- read.csv('myDF', header = TRUE)

#foo <- foo[,order(names(foo))]
# generate empty storage vector

storage <- rep(0,ncol(foo))

#for (i in 1:ncol(foo)){
#  storage[i] = 0.5*var(foo[,i]) - 2*mean(foo[,i])
#}
numIts<-foo[2,1]
newDf <- tail(foo, numSamples) #find a way to generalise this
newStorage <- rep(0,ncol(newDf))

for (i in 1:ncol(newDf)){
  newStorage[i] <- 0.5*var(newDf[,i]) - 2*mean(newDf[,i])
}

# myData <- data.frame(x,newStorage)

# write.table(myData[order(newStorage),],file = 'DICVs_ordered.txt')
x <- seq(min(foo[1,]),max(foo[1,])) 
df <- data.frame(newStorage,x)

write.table(df[order(newStorage),],file = 'DICVs_ordered.txt')

ggplot(df, aes(x = x, y = newStorage)) + geom_line() + theme_minimal() + theme(plot.title = element_text(hjust = 0.5)) + 
  labs(x = 'No. of Classes', y = 'DICV') + ggtitle('Information Criterion') + theme(plot.title = element_text(hjust = 0.5), text = element_text(size = 24))

ggsave('DICV_Plot.pdf', plot = last_plot())
}

allFiles <- system('ls *.log', intern = TRUE)
for (foo in allFiles){
  fileName <- foo
  
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
  
  # df[,2] to df[,2+(numGp-1)] will be the mx Props
  mixPropdf <- tail(df[grep('mixProp', colnames(df))],n=numSamples)
  mixPropMeans <- colMeans(mixPropdf)
  write.table(mixPropMeans, file = paste(fileName,'MixPropMeans.txt',sep = ''))
  
  mixPropdf$iter <- iterSeq
  mixPropdf <- melt(mixPropdf, id.vars = 'iter')
  
 
  
}

