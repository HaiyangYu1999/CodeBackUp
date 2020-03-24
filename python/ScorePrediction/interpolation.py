#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def lagrange(xi,yi,x):
    val=0
    if len(xi)!=len(yi):
        raise ValueError("size of x y not match")
    for i in range(len(xi)):
        p=1
        for j in range(len(xi)):
            if j!=i:
                p*=(x-xi[j])/(xi[i]-xi[j])
        p*=yi[i]
        val+=p
    return val


def dif(xi,yi):
    if len(xi)!=len(yi):
        raise ValueError("size of x y not match")
    diff=np.zeros((len(xi),len(yi)))
    for i in range(len(xi)):
        diff[i][0]=yi[i]
    for i in range(1,len(xi)):
        for j in range(i,len(xi)):
            diff[j][i]=(diff[j-1][i-1]-diff[j][i-1])/(xi[j-i]-xi[j])
    return diff


def newton(xi,yi,x):
    diff=dif(xi,yi)
    val=0
    tmp=1
    for i in range(len(xi)):
        val+=tmp*diff[i][i]
        tmp*=(x-xi[i])
    return val


if __name__=="__main__":
    x=[13,15,16,18,19,20]
    y=[3036.8,2699.3,2332.1,3295.5,3614.7,4060.3]
    print(lagrange(x, y, 14))
    print(newton(x,y,14))
    X=np.linspace(13,20,num=100)
    Y=newton(x,y,X)
    plt.plot(X,Y)
    plt.plot(x,y,'bo')
    plt.plot(14,lagrange(x, y, 14),'ro')
    plt.show()