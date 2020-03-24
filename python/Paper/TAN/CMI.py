#!/usr/bin/env python3
import numpy as np
import math


class CMI(object):
    def __init__(self,data,cmi1,cmi2):
        self.data=data
        self.cmi1=cmi1
        self.cmi2=cmi2
        self.m=np.size(data,1)

    def N(self,xi,xj,c):
        n=0
        for k in range(self.m):
            if self.data[7][k]==c and self.data[self.cmi1][k]==xi:
                if self.data[self.cmi2][k]==xj:
                    n+=1
        return n

    def N1(self,xi,c):
        n=0
        for k in range(self.m):
            if self.data[7][k]==c and self.data[self.cmi1][k]==xi:
                n+=1
        return n

    def N2(self,xj,c):
        n=0
        for k in range(self.m):
            if self.data[7][k]==c and self.data[self.cmi2][k]==xj:
                n+=1
        return n

    def Nc(self,c):
        n = 0
        for k in range(self.m):
            if self.data[7][k] == c:
                n += 1
        return n

    def Cmi(self):
        I=0
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    P_xi_xj_c=self.N(i,j,k)/self.m
                    P_c=self.Nc(k)/self.m
                    P_xi_c=self.N1(i,k)/self.m
                    P_xj_c=self.N2(j,k)/self.m
                    if P_xi_xj_c==0 or P_xj_c==0 or P_xi_c==0:
                        info=0
                    else:
                        fac=(P_c*P_xi_xj_c)/(P_xi_c*P_xj_c)
                        info=P_xi_xj_c*math.log(fac,2)
                    I+=info
        return I


if __name__=="__main__":
    data=np.loadtxt('dataAfterDiscrete.txt')
    cinfo=np.zeros((7,7))
    for i in range(7):
        for j in range(7):
            cmi=CMI(data,i,j)
            cinfo[i][j]=cmi.Cmi()
    np.savetxt('MutualInformation.txt',cinfo,delimiter=',')
    for i in range(7):
        print('{',end='')
        for j in range(7):
            s=',' if j<6 else ''
            print("{}{}".format(round(cinfo[i][j],4),s),end='')
        print('}')

