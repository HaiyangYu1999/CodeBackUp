t1=proc.time()
start3=Sys.time()
library(package="TDA")
trainClassification=read.csv("./TrainCloudClass.txt",header = FALSE)
testClassification=read.csv("./TestCloudClass.txt",header=FALSE)

step=11
d=14

trainSize=nrow(trainClassification)
testSize=nrow(testClassification)

loadSeparately=function()
{
  distance=matrix(data=0,nrow=testSize,ncol=trainSize)
  for(i in 1:testSize)
  {
    for(j in 1:trainSize)
    {
      trainTMPMatrix=scan(paste('./TimeTest/TrainCloud',j-1,'.txt',sep = ""))
      trainTMPMatrix=matrix(trainTMPMatrix, ncol = d, byrow = TRUE)
      testTMPMatrix=scan(paste('./TimeTest/TestCloud',i-1,'.txt',sep = ""))
      testTMPMatrix=matrix(testTMPMatrix, ncol = d, byrow = TRUE)
      trainDiag=ripsDiag(X=trainTMPMatrix, maxdimension=1, maxscale=10,dist="euclidean")
      testDiag=ripsDiag(X=testTMPMatrix, maxdimension=1, maxscale=10,dist="euclidean")
      distance[i,j]=wasserstein(Diag1=testDiag[["diagram"]],Diag2=trainDiag[["diagram"]],dimension=0)
    }
  }
  write.csv(distance,"WassersteinDistMatrix.csv")
}

loadSeparately()
end3=Sys.time()
#print(end3-start3)
t2=proc.time()
print(t2-t1)