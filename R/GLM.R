NegLoglik=function(X,y,b){
  eta=X%*%b
  p=exp(eta)/(1+exp(eta))
  lik_vec=ifelse(y==1,log(p),log(1-p))
  Loglik=sum(lik_vec)
    return(-Loglik)
}

NegLoglin_Poission=function(X,y,b){
  u=exp(X%*%b)
  lik_vec=y*log(u)-u-log(factorial(y))
  Loglik=sum(lik_vec)
  return(-Loglik)
}

donner=read.table("donner.txt") ## choose donner.txt
survive=donner[,3]
age=donner[,1]
sex=donner[,2]
const_x=rep(1,time=length(survive))
colnames(donner)=c("age","sex","survive")
head(donner)
x=t(rbind(const_x,age,sex))
y=survive

b.ini=rep(0,time=ncol(x))
  optim(fn=NegLoglik, X=x, y=y, par=b.ini) 
  #By default `optim` searches for parameters, which minimize the function `fn`.


model=glm(survive~age+sex, data=donner, family=binomial("logit"))
summary(model)$coefficients


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
