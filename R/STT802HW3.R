rm(list=ls())
N=50000
rate=2
shape=2
X=rgamma(N,rate=rate,shape=shape)
p=c(.1,.2,.3,.4,.5,.6,.7,.8,.9)
gamma22=function(x)
{
  return(dgamma(x,rate=2,shape = 2))
}
hist(X,200,freq = FALSE)
curve(gamma22,0,6,add=TRUE)
empQtl=quantile(X,p)
print(empQtl)
trueQtl=qgamma(p,shape=2,rate=2)
print(trueQtl)


N=50000
df=4
x=rchisq(N,df=df)
y=rep(0,N)
for(i in 1:N)
{
  y[i]=rnorm(1)*sqrt(df)/sqrt(x[i])
}
plot(density(y),col='blue')
norm=function(x)
{
  return(dnorm(x,0,1))
}
curve(norm,add=T)

df=100
x=rchisq(N,df=df)
y=rep(0,N)
for(i in 1:N)
{
  y[i]=rnorm(1)*sqrt(df)/sqrt(x[i])
}
plot(density(y),col='blue')
norm=function(x)
{
  return(dnorm(x,0,1))
}
curve(norm,col='red',add=T)

set.seed(1001)
s11=matrix(c(1,0.2,0.2,1.2),nrow=2)
s11Inv=solve(s11)
s12=c(0.3,0.1)
s21=t(s12)
s22=2
s22g1=s22-s21%*%s11Inv%*%s12
mu1=c(1,2)
mu2=0
N=30000
X=matrix(0,nrow=N,ncol=3)
for(i in 1:N)
{
  x1=rnorm(1,mean=1,sd=1)
  x2=rnorm(1,mean=1.8+0.2*x1,sd=1.4)
  x1v=c(x1,x2)
  mu3=mu2+s21%*%s11Inv%*%(x1v-mu1)
  x3=rnorm(1,mean=mu3,sd=sqrt(s22g1))
  X[i,]=c(x1,x2,x3)
}
cat(mean(X[,1]),mean(X[,2]),mean(X[,3]))
print(cov(X))



