import numpy as np
import pandas as pd

#datacsv=pd.read_csv('random_data.csv',header=None,sep=',')
#data=datacsv.values.T
data=np.loadtxt('originaldiscrete.txt')
data_new=np.zeros((4,40))
for i in range(40):
    if data[2][i]==1:
        data_new[0][i]=1
    elif data[2][i]==2:
        data_new[1][i]=1
    elif data[2][i]==3:
        data_new[2][i]=1
    elif data[2][i]==4:
        data_new[3][i]=1
datain=np.loadtxt('originaldiscrete1.txt')
data=np.zeros((7,40))
data[0]=datain[0]
data[1]=datain[1]
data[2]=data_new[0]
data[3]=data_new[1]
data[4]=data_new[2]
data[5]=data_new[3]
data[6]=datain[3]
np.savetxt('test_new.txt',data)