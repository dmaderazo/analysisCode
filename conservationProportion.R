
# script assumes that 3wayGetCharFreqs has been run
# Required for arrange function
library(tidyverse)

gpCharacterFreqs <- read.csv('gpData.csv',header=TRUE) #substitute your output file from 3wayGetCharFreqs

# Names of relevant columns
consNames <- c('X000gpNum','a','v')

consDataFrame <- gpCharacterFreqs[consNames]

consDataFrame$consProp <- NA

consDataFrame['consProp'] <- consDataFrame['a'] + consDataFrame['v']

consDataFrame %>% arrange(desc(consProp))

my_data = consDataFrame %>% arrange(desc(consProp))

write.csv(my_data, file = "consProp.txt")