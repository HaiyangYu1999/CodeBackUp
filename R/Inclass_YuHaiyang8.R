data=read.table('gout.txt',header=T,stringsAsFactors=F)
data$isMale=ifelse(data$sex=='M',1,0)
data$isBlack=ifelse(data$race=='B',1,0)
data$gout2=ifelse(data$gout=='N',0,1)
x=cbind(data$isMale,data$isBlack,data$age,data$gout2)
nRep=5000
n=nrow(x)


oddsRatioMF=rep(NA,nRep)
oddsRatioBW=rep(NA,nRep)
prWF55=rep(NA,nRep)
prBF55=rep(NA,nRep)
prWM55=rep(NA,nRep)
prBM55=rep(NA,nRep)
for(i in 1:nRep)
{
  tmp=sample(1:n,size=n,replace=T)
  tmpData=data[tmp,]
  fm=glm(tmpData$gout2~tmpData$isMale+tmpData$isBlack+tmpData$age,data=tmpData,family='binomial')
  betaSex=coef(fm)[2]
  betaRace=coef(fm)[3]
  coeffi=as.matrix(coef(fm))
  oddsWF55=exp(cbind(1,0,0,55)%*%coeffi)
  probWF55=oddsWF55/(1+oddsWF55)
  oddsBF55=exp(cbind(1,0,1,55)%*%coeffi)
  probBF55=oddsBF55/(1+oddsBF55)
  oddsWM55=exp(cbind(1,1,0,55)%*%coeffi)
  probWM55=oddsWM55/(1+oddsWM55)
  oddsBM55=exp(cbind(1,1,1,55)%*%coeffi)
  probBM55=oddsBM55/(1+oddsBM55)
  oddsRatioMF[i]=exp(betaSex)
  oddsRatioBW[i]=exp(betaRace)
  prWF55[i]=probWF55
  prBF55[i]=probBF55
  prWM55[i]=probWM55
  prBM55[i]=probBM55
}

print("OddsRatio(M/F)")
cat("mean =",mean(oddsRatioMF))
print(quantile(oddsRatioMF,c(0.025,0.975)))
print("OddsRatio(B/W)")
cat("mean =",mean(oddsRatioBW))
print(quantile(oddsRatioBW,c(0.025,0.975)))
print("ProbWF55")
cat("mean =",mean(prWF55))
print(quantile(prWF55,c(0.025,0.975)))
print("ProbBF55")
cat("mean =",mean(prBF55))
print(quantile(prBF55,c(0.025,0.975)))
print("ProbWM55")
cat("mean =",mean(prWM55))
print(quantile(prWM55,c(0.025,0.975)))
print("ProbBM55")
cat("mean =",mean(prBM55))
print(quantile(prBM55,c(0.025,0.975)))
