#1
H0_inverse1=function(x,lambda,nu)
{
  return(exp(log(x/lambda)/nu))
}

simExp=function(n,lambda,z,beta,nu)
{
  u=runif(n)
  tmp=-log(u)/exp(as.matrix(z)%*%beta)
  X=H0_inverse1(tmp,lambda,nu)
  return(X)
}
set.seed(12345)
lambda=1
beta=c(1,2)
n=100
z1=rbinom(n,1,0.5)
z2=rbinom(n,1,0.5)
z=cbind(z1,z2)
nu1=0.5
nu2=5
X1=simExp(n,lambda,z,beta,nu1)
X2=simExp(n,lambda,z,beta,nu2)
summary(X1)
hist(X1)
summary(X2)
hist(X2)

#2

H0_inverse2=function(x,lambda,alpha)
{
  return(log(alpha*x/lambda+1)/alpha)
}
simExp=function(n,lambda,z,beta,alpha)
{
  u=runif(n)
  tmp=-log(u)/exp(as.matrix(z)%*%beta)
  X=H0_inverse2(tmp,lambda,alpha)
  return(X)
}
set.seed(12345)
lambda=1
alpha=5
beta=c(1,2)
n=100
z1=rbinom(n,1,0.5)
z2=runif(n,0,3)
z=cbind(z1,z2)
X=simExp(n,lambda,z,beta,alpha)
summary(X)
hist(X)

#3

p=1000
n=400
iteration=1000
index=n/log(n)
PIT=0
sigma=matrix(NA,nrow=p,ncol=p)
for(i in 1:p)
{
  for(j in 1:p)
  {
    sigma[i,j]=0.5^abs(i-j)
  }
}
library(MASS)
for(rep in 1:iteration)
{
  set.seed(12345+rep)
  X=mvrnorm(n=n,mu=rep(0,p),Sigma=sigma)
  eps=rnorm(n,0,1)
  y=3*X[,1]+3*X[,2]+3*X[,3]+3*X[,4]+eps
  
  beta=rep(0,p)
  
  
  for(s in 1:p)
  {
    fit=lm(y~X[,s])
    beta[s]=-abs(coef(fit)[2])
  }
  beta=rank(beta)
  pit=0
  if((beta[1]<index)&&(beta[2]<index)&&(beta[3]<index)&&(beta[4]<index))
  {
    pit=1
  }
    
  PIT=PIT+pit
}
PIT=PIT/iteration
print(PIT)

#4
p=1000
n=400
iteration=100
index=n/log(n)
PIT=0
sigma=matrix(NA,nrow=p,ncol=p)
for(i in 1:p)
{
  for(j in 1:p)
  {
    if(i!=j)
      sigma[i,j]=0.5
    else
      sigma[i,j]=1
  }
}
library(MASS)
for(rep in 1:iteration)
{
  set.seed(12345+rep)
  X=mvrnorm(n=n,mu=rep(0,p),Sigma=sigma)
  eps=rnorm(n,0,1)
  y=3*X[,1]+3*X[,2]+3*X[,3]+3*X[,4]+3*X[,5]-7.5*X[,6]+eps
  
  beta=rep(0,p)
  
  
  for(s in 1:p)
  {
    fit=lm(y~X[,s])
    beta[s]=-abs(coef(fit)[2])
  }
  beta=rank(beta)
  pit=0
  if((beta[1]<index)&&(beta[2]<index)&&(beta[3]<index)&&(beta[4]<index)&&(beta[5]<index)&&(beta[6]<index))
  {
    pit=1
  }
  
  PIT=PIT+pit
}
PIT=PIT/iteration
print(PIT)

#5

p=1000
n=400
iteration=100
index=n/log(n)
PIT=0
sigma=matrix(NA,nrow=p,ncol=p)
for(i in 1:p)
{
  for(j in 1:p)
  {
    if(i!=j)
      sigma[i,j]=0.5
    else
      sigma[i,j]=1
  }
}
library(MASS)
for(rep in 1:iteration)
{
  set.seed(12345+rep)
  X=mvrnorm(n=n,mu=rep(0,p),Sigma=sigma)
  eps=rnorm(n,0,1)
  y=3*X[,1]+3*X[,2]+3*X[,3]+3*X[,4]+3*X[,5]-7.5*X[,6]+eps
  
  beta=rep(0,p-1)
  
  
  for(s in 2:p)
  {
    fit=lm(y~X[,1]+X[,s])
    beta[s-1]=-abs(coef(fit)[3])
  }
  beta=rank(beta)
  pit=0
  if((beta[1]<index)&&(beta[2]<index)&&(beta[3]<index)&&(beta[4]<index)&&(beta[5]<index))
  {
    pit=1
  }
  
  PIT=PIT+pit
}
PIT=PIT/iteration
print(PIT)

