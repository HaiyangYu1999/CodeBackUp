import numpy as np
import matplotlib.pyplot as plt
import random
import time
y=[1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1,
   1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1,
   0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1,
   1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0]

def f(y,pi,p,q):
    if y==1:
        res=pi*p+(1-pi)*q
    else:
        res=pi*(1-p)+(1-pi)*(1-q)
    return -np.log(res)

def F(pi,p,q):
    sm=0
    for i in range(len(y)):
        sm+=f(y[i],pi,p,q)
    return sm

def Q(mu,y,pi,p,q):
    n=len(mu)
    res=0
    for i in range(n):
        tmp=mu[i]*np.log(pi*p**y[i]*(1-p)**(1-y[i]))+(1-mu[i])*np.log((1-pi)*q**y[i]*(1-q)**(1-y[i]))
        res+=tmp
    return -res
def dQdpi(mu,y,pi,p,q):
    n = len(mu)
    res = 0
    for i in range(n):
        tmp=(mu[i]-pi)/(pi*(1-pi))
        res+=tmp
    return -res

def dQdp(mu,y,pi,p,q):
    n = len(mu)
    res = 0
    for i in range(n):
        tmp=mu[i]*(y[i]-p)/(p*(1-p))
        res+=tmp
    return -res
def dQdq(mu,y,pi,p,q):
    n = len(mu)
    res = 0
    for i in range(n):
        tmp=(1-mu[i])*(y[i]-q)/(q*(1-q))
        res+=tmp
    return -res

def emIter():
    n = len(y)
    alpha = 0.00001
    yarr = []
    pi = 0.5
    p = 0.5
    q = 0.5
    yarr.append(F(pi, p, q))
    k = 0
    x = [0]
    mu=np.zeros((n,1))
    while k<2500:
        for i in range(n):
            if y[i]==1:
                mu[i]=pi*p/(pi*p+(1-pi)*q)
            else:
                mu[i]=pi*(1-p)/(pi*(1-p)+(1-pi)*(1-q))
        for iter in range(1000):
            pi=pi-alpha*dQdpi(mu,y,pi,p,q)
            p = p - alpha * dQdp(mu, y, pi, p, q)
            q = q - alpha * dQdq(mu, y, pi, p, q)
            k+=1
            if k % 10 == 0:
                yarr.append(F(pi,p,q))
                x.append(k)
    plt.plot(x, yarr)
    plt.show()
    print()

emIter()