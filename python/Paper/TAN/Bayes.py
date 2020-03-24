#!/usr/bin/env python3
import numpy as np
from math import log
from TAN.CMI import CMI


class Prediction(object):
    def __init__(self,train,test):
        self.train=train
        self.test=test
        self.parray=[]
        self.clas=0
        for c in range(5):
            self.parray.append(self.Naiveprob(c))
        self.logp=self.parray[0]
        for i in range(1,len(self.parray)):
            if self.parray[i]>self.logp:
                self.logp=self.parray[i]
                self.clas=i

    def P_xi_pxi_c(self,xi,pxi,xi_value,pxi_value,c):
        cmi=CMI(self.train,xi,pxi)
        a=cmi.N(xi_value,pxi_value,c)+1
        b=cmi.N2(pxi_value,c)+5
        return a/b

    def P_x0_c(self,x0,x0_value,c):
        cmi=CMI(self.train,x0,1)
        a=cmi.N1(x0_value,c)+1
        b=cmi.Nc(c)+5
        return a/b

    def P_c(self,c):
        cmi=CMI(self.train,0,1)
        a=cmi.Nc(c)
        b=np.size(train,1)
        return a/b

    def prob(self,c):
        p53=self.P_xi_pxi_c(5,6,self.test[5],self.test[6],c)
        p36=self.P_xi_pxi_c(2,1,self.test[2],self.test[1],c)
        p26=self.P_xi_pxi_c(1,4,self.test[1],self.test[4],c)
        p60=self.P_xi_pxi_c(4,6,self.test[4],self.test[6],c)
        p14=self.P_xi_pxi_c(6,3,self.test[6],self.test[3],c)
        p40=self.P_xi_pxi_c(3,0,self.test[3],self.test[0],c)
        p0=self.P_x0_c(0,self.test[0],c)
        pc=self.P_c(c)
        p=log(pc)+log(p53)+log(p36)+log(p26)+log(p60)+log(p14)+log(p40)+log(p0)
        return p

    def Naiveprob(self,c):
        p=0
        for i in range(7):
            p+=log(self.P_x0_c(i,self.test[i],c))
        p+=log(self.P_c(c))
        return p


if __name__=="__main__":
    for s in range(5):
        train=np.loadtxt('Training{}.txt'.format(s))
        tes=np.loadtxt('Test{}.txt'.format(s))
        tp=0
        tn=0
        fp=0
        fn=0
        P=R=F1=0
        for i in range(np.size(tes,1)):
            t=tes[:,i]
            s=Prediction(train,t)
            if s.clas<3 and t[7]<3:
                tp+=1
            if s.clas<3 and t[7]>3:
                fp+=1
            if s.clas>3 and t[7]<3:
                fn+=1
            if s.clas>3 and t[7]>3:
                tn+=1
        P=tp/(tp+fp)
        R=tp/(tp+fn)
        F1=2*P*R/(P+R)
        print('P=',P,',R=',R,',F1=',F1)
