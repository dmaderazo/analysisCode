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

ggplot(df, aes(x = x, y = storage)) + geom_line() + theme_minimal() + theme(plot.title = element_text(hjust = 0.5)) + 
  labs(x = 'No. of Classes', y = 'DICV') + ggtitle('Information Criterion') + theme(plot.title = element_text(hjust = 0.5), text = element_text(size = 24))

#library(reshape2)
#ggplot(foo, aes(value)) + geom_line() 
