DATA=read.table('wages.txt',header=T)
n=nrow(DATA)
nTst=150
nRep=10
R2.TST1=rep(NA,nRep)
R2.TST2=rep(NA,nRep)
R2.TRN1=rep(NA,nRep)
R2.TRN2=rep(NA,nRep)
R2.TRNAdj1=rep(NA,nRep)
R2.TRNAdj2=rep(NA,nRep)
AIC1=rep(NA,nRep)
AIC2=rep(NA,nRep)
BIC1=rep(NA,nRep)
BIC2=rep(NA,nRep)


fm0=lm(Wage~1,data=DATA)
fm1=lm(Wage~Sex+Education+Experience,data=DATA) 
fm2=lm(Wage~.,data=DATA)

print(summary(fm1)[8])
print(summary(fm2)[8])
print(summary(fm1)[9])
print(summary(fm2)[9])
print(AIC(fm1))
print(AIC(fm2))
print(BIC(fm1))
print(BIC(fm2))
f=summary(fm1)$fstatistic
pvalue1=1-pf(f[1],f[2],f[3])
print(pvalue1)
f=summary(fm1)$fstatistic
pvalue2=1-pf(f[1],f[2],f[3])
print(pvalue2)


for(i in 1:nRep)
{
  tst=sample(1:n,size=nTst)
  TRN.DATA=DATA[-tst,]
  TST.DATA=DATA[tst,]
  fm0=lm(Wage~1,data=TRN.DATA)
  fm1=lm(Wage~Sex+Education+Experience,data=TRN.DATA) 
  fm2=lm(Wage~.,data=TRN.DATA)
  yHat0=predict(fm0,newdata=TST.DATA)
  yHat1=predict(fm1,newdata=TST.DATA)
  yHat2=predict(fm2,newdata=TST.DATA)
  PRSS0=sum((TST.DATA$Wage-yHat0)^2)
  PRSS1=sum((TST.DATA$Wage-yHat1)^2)
  PRSS2=sum((TST.DATA$Wage-yHat2)^2)
  R2.TST1[i]=(PRSS0-PRSS1)/PRSS0
  R2.TST2[i]=(PRSS0-PRSS2)/PRSS0
  R2.TRN1[i]=summary(fm1)$r.squared
  R2.TRN2[i]=summary(fm2)$r.squared
  R2.TRNAdj1[i]=summary(fm1)$adj.r.squared
  R2.TRNAdj2[i]=summary(fm2)$adj.r.squared
  AIC1[i]=AIC(fm1)
  AIC2[i]=AIC(fm2)
  BIC1[i]=BIC(fm1)
  BIC2[i]=BIC(fm2)
}
cat("Model1_AIC, Model2_AIC=",mean(AIC1)," , ",mean(AIC2),sep="")
cat("Model1_BIC, Model2_BIC=",mean(BIC1)," , ",mean(BIC2),sep="")
cat("Training R-sq1, Training R-sq2=",mean(R2.TRN1)," , ",mean(R2.TRN2))
cat("Training Adj R-sq1, Training Adj R-sq2=",mean(R2.TRNAdj1)," , ",mean(R2.TRNAdj2))
cat("prediction r-sq1 , prediction r-sq2 =",mean(R2.TST1),",",mean(R2.TST2))