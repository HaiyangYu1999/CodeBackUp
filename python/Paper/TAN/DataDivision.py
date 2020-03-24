#!/usr/bin/env python3
import numpy as np


if __name__=="__main__":
    b=np.loadtxt('dataAfterDiscrete.txt')
    step=54
    for i in range(5):
        begin=i*step
        end=(i+1)*step
        test=b[:,begin:end]
        train=np.delete(b,range(begin,end),axis=1)
        np.savetxt('Test{}.txt'.format(i),test)
        np.savetxt('Training{}.txt'.format(i),train)