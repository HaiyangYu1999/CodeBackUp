import numpy as np
import pandas as pd
import tensorflow as tf
import random
import statistics

TrainSetRatio=0.7

method=["mean","KNN","HD"]
i_index=[1,2,3]
j_index=range(20,100,5)
ilen=len(i_index)
jlen=len(j_index)
meanErr=np.zeros((ilen,jlen))
KNNErr=np.zeros((ilen,jlen))
HDErr=np.zeros((ilen,jlen))
err=[meanErr,KNNErr,HDErr]
meanErrQtl=np.zeros((ilen,jlen))
KNNErrQtl=np.zeros((ilen,jlen))
HDErrQtl=np.zeros((ilen,jlen))
meanErrQtl2=np.zeros((ilen,jlen))
KNNErrQtl2=np.zeros((ilen,jlen))
HDErrQtl2=np.zeros((ilen,jlen))
errQtl=[meanErrQtl,KNNErrQtl,HDErrQtl]
errQtl2=[meanErrQtl2,KNNErrQtl2,HDErrQtl2]
nRep=10

for md in range(len(method)):
    for i in range(len(i_index)):
        for j in range(len(j_index)):
            errSample=np.zeros((nRep,1))
            for s in range(nRep):
                data = pd.read_csv("./imputation/data{}_{}-{}.csv".format(i_index[i],method[md],j_index[j]))
                m=data.iloc[:,0].size
                trainSize=round(m*TrainSetRatio)
                smpl=random.sample(range(m),trainSize)
                wholeSet=set(range(m))
                smplSet=set(smpl)
                testSet=wholeSet-smplSet
                smplC=list(testSet)
                train=data.iloc[smpl,:-1]
                y_Otrain=data.iloc[smpl,-1]
                test=data.iloc[smplC,:-1]
                y_Otest=data.iloc[smplC,-1]
                model=tf.keras.Sequential(
                    [tf.keras.layers.Dense(10,input_shape=(5,),activation='relu'),
                     tf.keras.layers.Dense(1)]
                )
                model.compile(optimizer='adam',loss='mse')
                x=train.iloc[:,1:]
                y=y_Otrain
                model.fit(x,y,epochs=200)
                y_estimate=model.predict(test.iloc[:,1:])
                y_test=y_Otest.values
                sum=0
                for s in range(len(y_test)):
                    sum+=(y_test[s]-y_estimate[s][0])**2
                sum/=len(y_test)
                errSample[s]=sum
            tmp=np.quantile(errSample,[0.025,0.975])
            errQtl[md][i][j]=tmp[0]
            errQtl2[md][i][j] = tmp[1]
            err[md][i][j]=statistics.mean(errSample)
for i in range(3):
    print(err[i])
for i in range(3):
    print(errQtl[i])
for i in range(3):
    print(errQtl2[i])



