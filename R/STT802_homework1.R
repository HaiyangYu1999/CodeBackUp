fib=function(n){
  if(n==0)
    return("0")
  else if(n==1)
    return("0, 1")
  f0=0
  f1=1
  str="0, 1"
  while(n-1){
    f=f0+f1
    f0=f1
    f1=f
    str=paste(paste(str,",",sep=""),f)
    n=n-1
  }
  return(str)
}
cat("Fibonacci(6)=",fib(6),sep="")

set.seed(12345)
day=0
stk=20
while(stk<=25){
  delta_stk=runif(1,-5,5)
  print(delta_stk)
  stk=stk+delta_stk
  day=day+1
}
print(day)



split.data=function(data,p,k){
  flag=rep(0,times=nrow(data))
  data=data.frame(flag,data)
  train=sample(1:nrow(data),nrow(data)*p,replace = F)
  data[train,1]=1
  train_set=data[train,]
  train_set=train_set[,-1]
  test=c()
  for(i in 1:nrow(data)){
    if(data[i,1]==0){
      test=append(test,i)
    }
  }
  test_set=data[test,]
  test_set=test_set[,-1]
  if(k==1){
    return(train_set)
  }
  else{
    return(test_set)
  }
}

crab=read.table("crab.txt")
data=crab
p=0.6
train=split.data(data,p,1)
hist(train[,1])
test=split.data(data,p,2)
hist(test[,1])



NegLoglin_Poission=function(X,y,b){
  u=exp(X%*%b)
  lik_vec=y*log(u)-u-log(factorial(y))
  Loglik=sum(lik_vec)
  return(-Loglik)
}

crab=read.table("crab.txt") ## choose crab.txt
id=crab[,1]
C=crab[,2]
S=crab[,3]
W=crab[,4]
Wt=crab[,5]
Sa=crab[,6]
const_x=rep(1,time=nrow(crab))
x=t(rbind(const_x,W))
y=Sa
colnames(crab)=c("id","C","S","W","Wt","Sa")
head(crab)

b.ini=rep(0,time=ncol(x))
optim(fn=NegLoglin_Poission, X=x, y=y, par=b.ini)

model=glm(Sa~W,data=crab, family=(poisson(link=log)))
summary(model)$coefficients
