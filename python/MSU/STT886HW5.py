import numpy as np
import matplotlib.pyplot as plt
import scipy.special as scs

x_len=1000
n=2019
p=0.5
np.random.seed(100)
x=np.random.binomial(n,p,x_len)
x_max=np.max(x)


def Pxn(x,n):    # P(X=x|N=n)
    pi=1
    for k in range(x_len):
        pi*=scs.comb(n,x[k])*(1/2**(n))
    return pi


