#####
# Get mix props

library(ggplot2)
library(reshape2)
library(dplyr)

#Read in the file that you want
foo <- system('find *.log -maxdepth 0 -not -type d', intern = TRUE)
fileName <- foo

command1 <- sprintf("head -n 1 %s > tempFile", fileName)
system(command1)

cPointCommand <- read.table(file = 'tempFile', header = FALSE)
cPointCommand <- t(cPointCommand)

flags <- c("-n", "-ng")

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

system('rm -rf tempFile')
system('rm -rf rTemp.r')

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

vecMixProps 
#Make a data frame
mixPropFrame = df[mixProps]


#
