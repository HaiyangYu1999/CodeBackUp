LN=c(30,50,100,200,500,1000,3000) 
nRep=5000
mu = 120
b1 = -3
b2 = c(0, 0.2, 0.3, 0.5)
powMat = matrix(NA, ncol=length(b2), nrow=length(LN)) 
for (i in 1:length(LN))
{
  N=LN[i]
  for (j in 1:length(b2))
  {
    PVALUES=rep(NA,nRep)
    for(Rep in 1:nRep)
    {
      isMale = c(rep(0, N/2),rep(1,N/2))
      fBMI=rnorm(N/2, mean=26.5,sd=30^.5)
      mBMI=rnorm(N/2, mean=27.4,sd=16.7^.5)
      BMI=c(fBMI,mBMI)
      Z =BMI-mean(BMI)
      error=rnorm(N, sd=300^.5)
      y = mu + isMale*b1 + Z*b2[j] + error
      fm=lsfit(y=y,x=cbind(isMale, Z))
      PVALUES[Rep] = ls.print(fm,print.it=F)[[2]][[1]][3,4]
    }
    powMat[i, j] = mean(PVALUES<.05)
  }
}
print(powMat)


for(i in 1:length(b2))
{
  x = LN
  y=powMat[,i]
  plot(x=x,y=y,type='l',xlab=paste("sample size, effect size =",b2[i]),ylab = "power")
}
print("The minimum sample size needed to achieve a power of at least 80% if the effect size is 0.3 is about 1375.")


LN=seq(1000,10000,1000) 
nRep=5000
mu = 120
b1 = -3
b2 = c(0.2)
powMat = matrix(NA, ncol=length(b2), nrow=length(LN)) 
for (i in 1:length(LN))
{
  N=LN[i]
  for (j in 1:length(b2))
  {
    PVALUES=rep(NA,nRep)
    for(Rep in 1:nRep)
    {
      isMale = c(rep(0, N/2),rep(1,N/2))
      fBMI=rnorm(N/2, mean=26.5,sd=30^.5)
      mBMI=rnorm(N/2, mean=27.4,sd=16.7^.5)
      BMI=c(fBMI,mBMI)
      Z =BMI-mean(BMI)
      error=rnorm(N, sd=300^.5)
      y = mu + isMale*b1 + Z*b2[j] +isMale*Z*(0.4-0.2) + error
      fm=lsfit(y=y,x=cbind(isMale, Z,isMale*Z))
      PVALUES[Rep] = ls.print(fm,print.it=F)[[2]][[1]][4,4]
    }
    powMat[i, j] = mean(PVALUES<.05)
  }
}
print(powMat)


print("Thus, a power of at least 50% can be achieved with a sample size <= 10,000.")
