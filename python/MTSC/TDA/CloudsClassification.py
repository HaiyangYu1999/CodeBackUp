#!usr/bin/env python3


import pandas as pd
import numpy as np
trainClass=pd.read_csv("./TrainSetClassification.csv",header=None)
testClass=pd.read_csv("./TestSetClassification.csv",header=None)
step=10
trainCloudSize=int(trainClass.shape[0]/step)
testCloudSize=int(testClass.shape[0]/step)
trainCloudClass=np.zeros((trainCloudSize,1))
testCloudClass=np.zeros((testCloudSize,1))
trainCloudClassIndex=0
testCloudClassIndex=0
trainCloudTMP=0
testCloudTMP=0
for i in range(trainClass.shape[0]):
    trainCloudTMP += trainClass.values[i]
    if i % step == step-1:
        trainCloudClass[trainCloudClassIndex]= 0 if trainCloudTMP==0 else 1
        trainCloudClassIndex +=1
        trainCloudTMP=0
for i in range(testClass.shape[0]):
    testCloudTMP += testClass.values[i]
    if i % step == step-1:
        testCloudClass[testCloudClassIndex]= 0 if testCloudTMP==0 else 1
        testCloudClassIndex +=1
        testCloudTMP=0

np.savetxt("./TrainCloudClass.txt",trainCloudClass,fmt="%f")
np.savetxt("./TestCloudClass.txt",testCloudClass,fmt="%f")
