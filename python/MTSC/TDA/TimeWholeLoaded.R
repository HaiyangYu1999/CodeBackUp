t1=proc.time()
start3=Sys.time()
library(package="TDA")
trainClassification=read.csv("./TrainCloudClass.txt",header = FALSE)
testClassification=read.csv("./TestCloudClass.txt",header=FALSE)

step=11
d=14

trainSize=nrow(trainClassification)
testSize=nrow(testClassification)

loadWhole=function()
{
  trainMatrix=scan("TrainCloudMatrix.txt")
  trainMatrix=matrix(trainMatrix,ncol=d,byrow=TRUE)
  
  testMatrix=scan("TestCloudMatrix.txt")
  testMatrix=matrix(testMatrix,ncol=d,byrow = TRUE)
  
  distance=matrix(data=0,nrow=testSize,ncol=trainSize)
  
  trainTMPMatrix=matrix(0,ncol=d,nrow=step)
  testTMPMatrix=matrix(0,ncol=d,nrow=step)
  
  for(i in 1:testSize)
  {
    for(j in 1:trainSize)
    {
      trainTMPMatrix=trainMatrix[(step*(j-1)+1):(step*j),]
      testTMPMatrix=testMatrix[(step*(i-1)+1):(step*i),]
      trainDiag=ripsDiag(X=trainTMPMatrix, maxdimension=1, maxscale=10,dist="euclidean")
      testDiag=ripsDiag(X=testTMPMatrix, maxdimension=1, maxscale=10,dist="euclidean")
      distance[i,j]=wasserstein(Diag1=testDiag[["diagram"]],Diag2=trainDiag[["diagram"]],dimension=0)
    }
  }
  write.csv(distance,"WassersteinDistMatrix.csv")
}

loadWhole()
end3=Sys.time()
#print(end3-start3)
t2=proc.time()
print(t2-t1)