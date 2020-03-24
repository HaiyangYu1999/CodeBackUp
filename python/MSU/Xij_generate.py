import pandas as pd
import numpy as np

N=[100,200,500]
for n in N:
    X=np.zeros((n,5))
    y=np.zeros((n,1))
    epsilon=np.random.normal(0,1,n)
    for i in range(n):
        e=np.random.normal(0,1)
        z=np.random.normal(0,1,5)
        X[i]=(e+z)/2
    y=10*X[:,1]/(1+X[:,0]*X[:,0])+5*np.sin(X[:,2]*X[:,3])+2*X[:,4]+epsilon
    data=pd.DataFrame({"y":y,"x1":X[:,0],"x2":X[:,1],"x3":X[:,2],"x4":X[:,3],"x5":X[:,4]})
    data.to_csv("Dataset{}.csv".format(n),index=False)

