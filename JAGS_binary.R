
rm( list = ls())

require(rjags)

# model specification

binaryClasModel <- function(){
  
    for(i in 1:N){ # N is the number of individuals
      for(j in 1:K){ # K is the number of classifiers
        
        # I
        class[j,i] ~ dbern(params[j,diseasepl[i]])
      }
      # Same as disease but with offset 1, instead of 0
      diseasepl[i] <- disease[i]+1
      # Actual disease status ie true classification
      disease[i] ~ dbern(pd)
    }
    # Distributions of classifier parameters
    for(j in 1:K){
      # Parameter for the distribution of the probability of getting a true positive
      params[j,1] ~ dunif(0,params[j,2])
      # Parameter for the distribution of the probability of getting a true negative
      params[j,2] ~ dunif(params[j,1],1)
      
      # Sensitivity
      sens[j] <- params[j,2]
      # Specificity
      spec[j] <- 1-params[j,1]
    }
    
    # Distribution of prevalence
    pd ~ dunif(0,1)
}
write.model(binaryClasModel,"binaryClassModel.txt")
model.file1 = paste(getwd(),"binaryClassModel.txt", sep="/")

modelString = "
model{
    for(i in 1:N){ # N is the number of individuals
      for(j in 1:K){ # K is the number of classifiers
        
        # I
        class[j,i] ~ dbern(params[j,diseasepl[i]])
      }
      # Same as disease but with offset 1, instead of 0
      diseasepl[i] <- disease[i]+1
      # Actual disease status ie true classification
      disease[i] ~ dbern(pd)
    }
    # Distributions of classifier parameters
    for(j in 1:K){
      # Parameter for the distribution of the probability of getting a true positive
      params[j,1] ~ dunif(0,params[j,2])
      # Parameter for the distribution of the probability of getting a true negative
      params[j,2] ~ dunif(params[j,1],1)
      
      # Sensitivity
      sens[j] <- params[j,2]
      # Specificity
      spec[j] <- 1-params[j,1]
    }
    
    # Distribution of prevalence
    pd ~ dunif(0,1)
}
# ... end of JAGS model specification
"

# Write the modelString to a file, using R commands:
writeLines(modelString,con="binaryClassModel.txt")
# initialise data list

mydf<-read.csv('chr12segs_classified')

dataMat <-t( data.matrix(mydf))
numRows <- nrow(mydf) #1000
numCols <- ncol(mydf) #3 

tfbsClassifications <- list(N=numRows,K=numCols,class=dataMat)

# initialise the intis

initsList <- tfbsClassifications

# inits <- function(){list(params=structure(.Data = rep(0.5,numCols*2), .Dim=c(numCols,2)),
#               pd=0.5 
# ) }


parameters = c("params", "sens", "spec")

adaptSteps = 500              # Number of steps to "tune" the samplers.
burnInSteps = 1000            # Number of steps to "burn-in" the samplers.
nChains = 3                   # Number of chains to run.
numSavedSteps=50000           # Total number of steps in chains to save.
thinSteps=1                   # Number of steps to "thin" (1=keep every step).
nIter = ceiling( ( numSavedSteps * thinSteps ) / nChains ) # Steps per chain.

# Create, initialize, and adapt the model:
jagsModel = jags.model( "binaryClassModel.txt" , data=dataList , inits=initsList ,
                        n.chains=nChains , n.adapt=adaptSteps )

# Burn-in:
cat( "Burning in the MCMC chain...\n" )
update( jagsModel , n.iter=burnInSteps )
# The saved MCMC chain:
cat( "Sampling final MCMC chain...\n" )
codaSamples = coda.samples( jagsModel , variable.names=parameters ,
                            n.iter=nIter , thin=thinSteps )
# resulting codaSamples object has these indices:
#   codaSamples[[ chainIdx ]][ stepIdx , paramIdx ]

mcmcChain = as.matrix( codaSamples )





