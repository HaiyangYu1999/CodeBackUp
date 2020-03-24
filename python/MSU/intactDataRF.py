import numpy as np
import pandas as pd
import random
from sklearn.ensemble import RandomForestRegressor
TrainSetRatio=0.7
i_index=[1,2,5]
nRep=10
ilen=len(i_index)
error=np.zeros((ilen,1))
for i in range(ilen):
    averageSum = 0
    data=pd.read_csv("Dataset{}00(1).csv".format(i_index[i]))
    for _ in range(nRep):
        m = data.iloc[:, 0].size
        trainSize = round(m * TrainSetRatio)
        smpl = random.sample(range(m), trainSize)
        wholeSet = set(range(m))
        smplSet = set(smpl)
        testSet = wholeSet - smplSet
        smplC = list(testSet)
        train = data.iloc[smpl, :-1]
        y_Otrain = data.iloc[smpl, -1]
        test = data.iloc[smplC, :-1]
        y_Otest = data.iloc[smplC, -1]
        rf = RandomForestRegressor(n_estimators=100, random_state=42)
        x = train
        y = y_Otrain
        rf.fit(x, y)
        y_estimate = rf.predict(test)
        y_test = y_Otest.values
        sum = 0
        for s in range(len(y_test)):
            sum += (y_test[s] - y_estimate[s]) ** 2
        sum /= len(y_test)
        averageSum += sum
    averageSum/=nRep
    error[i]=averageSum
print(error)