set.seed(1000)
N=10000
P=matrix(NA,2,2)
X=rep(NA,N)
Y=rep(NA,N)
Px=0.8
Py=0.7
X[1]=rbinom(1,1,Px)
Y[1]=rbinom(1,1,Pygx[X[1]+1])
Pxgy=c(2/3,6/7)
Pygx=c(1/2,3/4)
for(i in 2:N)
{
  X[i]=rbinom(1,1,Pxgy[Y[i-1]+1])
  Y[i]=rbinom(1,1,Pygx[X[i]+1])
}

x00=0
x01=0
x10=0
x11=0
for(i in 1:N)
{
  if(X[i]==0&&Y[i]==0)
    x00=x00+1
  if(X[i]==0&&Y[i]==1)
    x01=x01+1
  if(X[i]==1&&Y[i]==0)
    x10=x10+1
  if(X[i]==1&&Y[i]==1)
    x11=x11+1
}

cat("mean(X)=",mean(X),sep="")
cat("mean(Y)=",mean(Y),sep="")
cat("      Y=0    Y=1")
cat("X=0",x00/N,x01/N)
cat("X=1",x10/N,x11/N)
