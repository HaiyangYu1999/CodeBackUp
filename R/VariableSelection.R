p=1000
n=200
rho=.5
rep=100
RANK=matrix(0,nrow=rep,ncol=p)
for(k in 1:rep)
{
  sigma=matrix(NA,nrow=p,ncol=p)
  for(i in 1:p)
  {
    for(j in 1:p)
    {
      if(i==j)
        sigma[i,j]=1
      else
        sigma[i,j]=rho
    }
  }
  library(MASS)
  set.seed(12345+k)
  X=mvrnorm(n=n,mu=rep(0,p),Sigma=sigma)
  Y=5*X[,1]+5*X[,2]+5*X[,3]+rnorm(n,0,1)
  
  beta=numeric(p)
  
  for(j in 1:p)
  {
    fit=lm(Y~X[,j])
    beta[j]=abs(coef(fit)[2])
    RANK[k,]=rank(-beta)
  }
  
}

b=rank(apply(RANK,2,mean))
for(i in 1:10)
{print(which(b==i))}



