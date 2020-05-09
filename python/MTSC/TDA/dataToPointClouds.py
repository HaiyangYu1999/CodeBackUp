import pandas as pd
import numpy as np

trainDf=pd.read_csv("./TrainDataNormalized.csv")
testDf=pd.read_csv("./TestDataNormalized.csv")

# add symmetry-breaking vector
dim=trainDf.shape[1]
for i in range(dim):
    trainDf.iloc[:,i]+=i
    testDf.iloc[:, i] += i

# add anchor point
step=10

#trainArray=trainDf.values
#testArray=testDf.values
trainTotalAnchor=int(trainDf.shape[0]/step)
testTotalAnchor=int(testDf.shape[0]/step)

trainCloudDim=(trainDf.shape[0]+trainTotalAnchor,dim)
testCloudDim=(testDf.shape[0]+testTotalAnchor,dim)
anchorPoint=np.zeros((1,dim))

trainCloud=np.zeros(trainCloudDim)
testCloud=np.zeros(testCloudDim)

trainCloudIndex=0
testCloudIndex=0

for i in range(trainDf.shape[0]):
    trainCloud[trainCloudIndex]=trainDf.iloc[i]
    trainCloudIndex += 1
    if i % step == step-1:
        trainCloud[trainCloudIndex] = anchorPoint
        trainCloudIndex += 1
np.savetxt("./TrainCloudMatrix.txt",trainCloud,fmt='%f')

for i in range(testDf.shape[0]):
    testCloud[testCloudIndex]=testDf.iloc[i]
    testCloudIndex += 1
    if i % step == step-1:
        testCloud[testCloudIndex] = anchorPoint
        testCloudIndex += 1
np.savetxt("./TestCloudMatrix.txt",testCloud,fmt='%f')

#This function is used to generate separate Cloud data matrix files
# and use R code load these files one by one.
# Compare to load a big file that contains all the matrix at a time.
def timeTestGenerator():
    row=step+1
    trainCloudMatrix=np.zeros((row,dim))
    testCloudMatrix=np.zeros((row,dim))
    for trainIndex in range(trainTotalAnchor):
        for i in range(step):
            trainCloudMatrix[i]=trainDf.iloc[trainIndex*step+i]
        trainCloudMatrix[step]=anchorPoint
        np.savetxt("./TimeTest/TrainCloud{}.txt".format(trainIndex),trainCloudMatrix,fmt="%f")
    for testIndex in range(testTotalAnchor):
        for i in range(step):
            testCloudMatrix[i]=testDf.iloc[testIndex*step+i]
        testCloudMatrix[step]=anchorPoint
        np.savetxt("./TimeTest/TestCloud{}.txt".format(testIndex),testCloudMatrix,fmt="%f")
    #copy comparison data to the same directory
    np.savetxt("./TimeTest/TrainCloudMatrix.txt", trainCloud, fmt='%f')
    np.savetxt("./TimeTest/TestCloudMatrix.txt", testCloud, fmt='%f')

#call this function
timeTestGenerator()