#!/usr/bin/env python3

import pandas as pd
trainDf=pd.read_csv("./TrainRawData.csv")
trainClass=trainDf.iloc[:,-1]                       #save classification data at -1 column
trainDf.drop(columns='EYE_STATUS',inplace=True)
testDf=pd.read_csv("./TestRawData.csv")
testClass=testDf.iloc[:,-1]
testDf.drop(columns='EYE_STATUS',inplace=True)
mean=trainDf.mean()
std=trainDf.std()                    # use the training set's mean and variation normalize test set
trainNormalized=(trainDf-mean)/std
testNormalized=(testDf-mean)/std
trainDf.iloc[:,-1]=trainClass
testDf.iloc[:,-1]=testClass
print(trainNormalized.describe())
print(testNormalized.describe())
trainNormalized.to_csv("./TrainDataNormalized.csv",index=False)
testNormalized.to_csv("./TestDataNormalized.csv",index=False)
trainClass.to_csv("./TrainSetClassification.csv",index=False,header=None)
testClass.to_csv("./TestSetClassification.csv",index=False,header=None)

