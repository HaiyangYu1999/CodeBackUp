#!/usr/bin/env python3
import pandas as pd
import numpy as np

if __name__=="__main__":
    data=pd.read_csv('dataPlusPrecipitation.txt',header=None,sep=' ')
    for j in range(8):
        vect=data.iloc[j]
        c=pd.qcut(vect,5,labels=[0,1,2,3,4])
        for i in range(len(vect)):
            pass
            data[i][j]=c[i]
    data=data.values
    np.savetxt('dataAfterDiscrete.txt',data)