phi=function(x)
{
  return(exp(-x^2/2)/sqrt(2*pi))
}
erf = function(x)
{
  return(2 * pnorm(x * sqrt(2)) - 1)
}
Phi=function(x)
{
  tmp=1+erf(x/sqrt(2))
  return(tmp/2)
}
set.seed(195021)
n=10
mu=4
v=2
y=rnorm(n,mean=mu,sd=sqrt(v))

isCensored=runif(n)<.2

yCen=y
yCen[isCensored]=y[isCensored]+runif(min=-1,max=-.02,n=sum(isCensored)) 
mu=rep(NA,n) # a vector to store estimates iterations
sigma=rep(NA,n)
mu[1]=mean(y[!isCensored]) # initial value (estimate ignoring censoring)
sigma[1]=var(y[!isCensored])
completeData=yCen  # this vector stores the 'complete' data
for(i in 2:length(mu)){
  # E-step
  alpha=(yCen[isCensored]-mu[i-1])/sqrt(sigma[i-1])
  z=1-Phi(alpha)
  mn=mu[i-1]+sqrt(sigma[i-1])*(phi(alpha)/z)
  completeData[isCensored]=mn
  mu[i]=mean(completeData)
  sigma[i]=var(completeData)
}
plot(mu)
plot(sigma)