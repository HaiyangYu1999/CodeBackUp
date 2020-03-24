import pandas as pd
import numpy as np


def discrete():
    data=pd.read_csv('discrete.csv',header=None,sep=',')
    data=data.T
    print(data)
    for j in range(2,4):
        vect=data.iloc[j]
        c=pd.qcut(vect,5,labels=[0,1,2,3,4])
        for i in range(len(vect)):
            pass
            data[i][j]=c[i]
    data=data.values
    np.savetxt('dataAfterDiscrete.txt',data)


class CNT(object):
    def __init__(self,data):
        self.data=data
        self.m=np.size(data,1)

    def Ngmat(self,xi,c):
        n=0
        for k in range(self.m):
            if self.data[1][k]==c and self.data[2][k]==xi:
                n+=1
        return n

    def Nrank(self,xi,c):
        n=0
        for k in range(self.m):
            if self.data[1][k]==c and self.data[4][k]==xi:
                n+=1
        return n

    def Ngpa(self,xj,c):
        n=0
        for k in range(self.m):
            if self.data[1][k]==c and self.data[3][k]==xj:
                n+=1
        return n

    def Nc(self,c):
        n = 0
        for k in range(self.m):
            if self.data[1][k] == c:
                n += 1
        return n


if __name__=="__main__":
    data1=np.loadtxt('dataAfterDiscrete.txt')
    p=30
    data=data1[:,:p]
    a=CNT(data)
    test=data1[:,p:]
    all=0
    right=0
    real = []
    for i in range(np.size(data,1)):
        c_real=data[1][i]
        gmat=data[2][i]
        rank=data[4][i]
        gpa=data[3][i]
        c=[0,1]
        p=[]
        for i in c:
            p1 = (a.Ngmat(gmat, i) + 1) / (a.Nc(i) + 5)
            p2 = (a.Ngpa(gpa, i) + 1) / (a.Nc(i) + 5)
            p3 = (a.Nrank(rank, i) + 1) / (a.Nc(i) + 4)
            p.append(p1*p2*p3)
        if p[0]>p[1]:
            c_pred=0
        else:
            c_pred=1
        if c_real==c_pred:
            right+=1
        real.append(c_pred)
        all+=1
    print(right/all)
