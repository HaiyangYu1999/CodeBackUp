#!/usr/bin/env python3

import pandas as pd

partition=0.8

df=pd.read_csv("RawData.txt")
length=df.shape[0]
trainLength=10*int(partition*length/10)             #ensure that data size can be divided by 10
trainDf=df.iloc[:trainLength]
testDf=df.iloc[trainLength:]
trainDf.to_csv("./TrainRawData.csv",index=False)
testDf.to_csv("./TestRawData.csv",index=False)

