import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
allData=pd.read_csv('score.csv',header=None,sep=',')
res=[]
for j in range(16):
    fig = plt.figure(figsize=(12, 8))
    x=[]
    for i in range(100):
        x.append(i+1)
    y = allData.iloc[:, j]
    y=np.array(y)
    f2=interp1d(x,y,'cubic')
    X=np.linspace(1,100,num=2000)
    Y=f2(98.5)
    res.append(Y)
print(res)
