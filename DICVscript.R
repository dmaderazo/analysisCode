rm(list = ls())

system('getLnDataframe.py -o myDF')

{
foo <- read.csv('myDF', header = TRUE)

#foo <- foo[,order(names(foo))]
# generate empty storage vector

storage <- rep(0,ncol(foo))

#for (i in 1:ncol(foo)){
#  storage[i] = 0.5*var(foo[,i]) - 2*mean(foo[,i])
#}
numIts<-foo[2,1]
newDf <- tail(foo, numIts) #find a way to generalise this
newStorage <- rep(0,ncol(newDf))

for (i in 1:ncol(newDf)){
  newStorage[i] <- 0.5*var(newDf[,i]) - 2*mean(newDf[,i])
}

myData <- data.frame(x,newStorage)

write.table(myData[order(newStorage),],file = 'DICVs_ordered.txt')



library(ggplot2)
x <- seq(min(foo[1,]),max(foo[1,])) 
df <- data.frame(newStorage,x)

ggplot(df, aes(x = x, y = newStorage)) + geom_line() + theme_minimal() + theme(plot.title = element_text(hjust = 0.5)) + 
  labs(x = 'No. of Classes', y = 'DICV') + ggtitle('Information Criterion') + theme(plot.title = element_text(hjust = 0.5), text = element_text(size = 24))

ggsave('DICV_Plot.pdf', plot = last_plot())
}

