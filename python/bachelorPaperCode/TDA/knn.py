import pandas as pd
import numpy as np


dis=pd.read_csv("./WassersteinDistMatrix.csv")
dis.drop(columns=dis.columns.values[0],inplace=True,axis=1)
dis=dis.values

testCloudSize=dis.shape[0]

valueTrue=pd.read_csv("./TestCloudClass.txt",header=None).values
classQuery=pd.read_csv("./TrainCloudClass.txt",header=None).values
valuePredict=np.zeros((testCloudSize,1))

#k=50             # select a variable k in kNN

for k in [5*x for x in range(1,20)]:
    for i in range(testCloudSize):
        distTmp=dis[i]
        # rank by ascending order and select top k nearest point
        rank=np.argsort(distTmp)[:k]
        classArray=classQuery[rank]
        valuePredict[i]=1 if sum(classArray)>k/2 else 0


 #evaluation
    TP=0
    FN=0
    FP=0
    TN=0
    res=np.zeros((testCloudSize,2))
    for i in range(testCloudSize):
        res[i]=[valueTrue[i][0],valuePredict[i][0]]
        if valuePredict[i][0]==1 and valueTrue[i][0]==1:
            TP +=1
        elif valuePredict[i][0]==1 and valueTrue[i][0]==0:
            FP +=1
        elif valuePredict[i][0]==0 and valueTrue[i][0]==1:
            FN +=1
        elif valuePredict[i][0]==0 and valueTrue[i][0]==0:
            TN +=1
    accuracy=(TP+TN)/(TP+FP+FN+TN)
    sensitivity=TP/ (TP+ FN)
    specificity=TN / (FP + TN)
    print(accuracy,sensitivity,specificity)
