 rm(list = ls())
foo <- read.csv('logLikelihoodFrame.txt', header = TRUE)

# generate empty storage vector

storage <- rep(0,ncol(foo))

for (i in 1:ncol(foo)){
  storage[i] = 0.5*var(foo[,i]) - 2*mean(foo[,i])
}

newDf <- tail(foo, n = 1000)
newStorage <- rep(0,ncol(newDf))

for (i in 1:ncol(newDf)){
  newStorage[i] <- 0.5*var(newDf[,i]) - 2*mean(newDf[,i])
}

library(ggplot2)
x <- seq(2,20) #GENERALIZE THIS
df <- data.frame(storage,x)

ggplot(df, aes(x = x, y = storage)) + geom_line() + theme_minimal()

#library(reshape2)
#ggplot(foo, aes(value)) + geom_line() 
