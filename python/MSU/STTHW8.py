import numpy as np
import matplotlib.pyplot as plt
#Birth and Death Processes with lambda=3 and mu=2
lmbd=3
mu=2
lenth=100
color=['r','teal','g','c','m','y','k','w','lime','aqua']
x0=10    #initial individuals
for j in range(10):
    x=x0
    np.random.seed(1000+j)
    xLst=[10]
    tLst=[0]
    time=0
    while True:
        t1=np.random.exponential(1/lmbd,1)[0]
        t2=np.random.exponential(1/mu,1)[0]
        if t1>t2:
            t=t2
            x-=1
        else:
            t=t1
            x+=1
        time+=t
        if time>lenth or x==0:
            break
        else:
            xLst.append(x)
            tLst.append(time)
    plt.scatter(tLst, xLst,s=0.5,color=color[j])
plt.savefig("STT886HW8.jpg")
plt.show()
