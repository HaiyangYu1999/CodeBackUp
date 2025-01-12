rm(list = ls())
q=3
sigma=matrix(NA,nrow=q,ncol=q)
for(i in 1:q)
{
  for(j in 1:q)
  {
    if(i==j)
    {
      sigma[i,j]=1
    }
    else
    {
      sigma[i,j]=0.5
    }
  }
}

nRep=10000
n=100
PVALUES=matrix(nrow=nRep,ncol=q,NA)
L=chol(sigma)
for(i in 1:nRep){
  X=matrix(NA,nrow=n,ncol=q)
  for(s in 1:n)
  {
    z=rnorm(3)
    X[s,]=L%*%z
  }
  y=rnorm(n)
  fm=lsfit(y=y,x=X)
  PVALUES[i,]=ls.print(fm,print.it=F)[[2]][[1]][,4][-1]
  if(i%%100){ message(i) }
}
mean(PVALUES[,1]<.05)
mean(PVALUES[,2]<.05)

mean(PVALUES[,1]<.05 | PVALUES[,2]<0.05 | PVALUES[,3]< 0.05)
mean(PVALUES[,1]<.05/3 | PVALUES[,2]<0.05/3 | PVALUES[,3]< 0.05/3)