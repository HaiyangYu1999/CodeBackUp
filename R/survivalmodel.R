H0_inverse=function(x,lambda)
{
  return(x/lambda)
}
set.seed(12345)
simExp=function(n,lambda,z,beta)
{
  u=runif(n)
  tmp=-log(u)/exp(as.matrix(z)%*%beta)
  X=H0_inverse(tmp,lambda)
  return(X)
}

lambda=1
beta=1
n=100
z=rbinom(n,1,0.5)

X=simExp(n,lambda,z,beta)
summary(X)
hist(X)



