N=c(30,50,100,200,500,1000,3000) # sample size
nRep=500 # number of Monte Carlo replicates
mu = 120
b1 = -3
b2 = c(0, 0.2, 0.3, 0.5)
pow_mat = matrix(NA, ncol=length(b2), nrow=length(N)) 
for (i in 1:length(N)){
  for (j in 1:length(b2)){
    PVALUES=matrix(NA, nrow=nRep,ncol=1)
    for(Rep in 1:nRep){
      M = rep(1, N[i])
      M[1:(N[i]/2)] = 0
      
      BMI = rep(NA, N[i])
      BMI[1:(N[i]/2)] = rnorm(N[i]/2, mean=26.5,sd=30^.5)
      BMI[(1+N[i]/2):N[i]] = rnorm(N[i]/2, mean=27.4,sd=16.7^.5)
      Z =BMI-mean(BMI)
      
      # SBP=mu+M*b1+Z*b2+error
      SBP = mu + M*b1 + Z*b2[j] + rnorm(N[i], sd=300^.5)
      fm=lsfit(y=SBP,x=cbind(M, Z))
      PVALUES[Rep,] = ls.print(fm,print.it=F)[[2]][[1]][3,4]
    }
    pow_mat[i, j] = mean(PVALUES<.05)
  }
}
pow_mat