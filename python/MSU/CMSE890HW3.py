import numpy as np
import matplotlib.pyplot as plt

def partial(x):
    tmp=A.dot(x)-b
    res=A.T.dot(tmp)
    return res

def prox(t,x):   #when h(x)=||x||_{1}
    res=np.zeros((len(x),1))
    for i in range(len(x)):
        if x[i]>t:
            res[i]=x[i]-t
        if x[i]<-t:
            res[i]=x[i]+t
    return res

def f(x):
    s1=0
    for i in range(len(x)):
        s1+=abs(x[i])
    tmp=A.dot(x)-b
    s2=np.dot(tmp.T,tmp)
    return s1+s2


np.random.seed(1000)
m=200
n=1000
A=np.random.normal(0,1,(m,n))
x_bar=np.zeros((n,1))
for i in range(20):
    k=np.random.randint(0,1000)
    x_bar[k]=np.random.normal(0,1)
b=A.dot(x_bar)

x_pre=np.zeros((n,1))
y1=[]
n1=[]
y2=[]
n2=[]
y3=[]
n3=[]
iteration=1000
for i in range(iteration):
    tk=0.0005
    x_now=prox(tk,x_pre-tk*partial(x_pre))
    x_pre=x_now
    if i%10==0 and i>20:
        y1.append(f(x_now)[0][0])
        n1.append(i)
x_pre=np.zeros((n,1))
for i in range(iteration):
    tk=0.0001
    x_now=prox(tk,x_pre-tk*partial(x_pre))
    x_pre=x_now
    if i%10==0 and i>20:
        y2.append(f(x_now)[0][0])
        n2.append(i)
x_pre=np.zeros((n,1))
for i in range(iteration):
    tk=0.00005
    x_now=prox(tk,x_pre-tk*partial(x_pre))
    x_pre=x_now
    if i%10==0 and i>20:
        y3.append(f(x_now)[0][0])
        n3.append(i)
plt.plot(n1,y1,label=r'$t_{k}=0.0005$')
plt.plot(n2,y2,label=r'$t_{k}=0.0001$')
plt.plot(n3,y3,label=r'$t_{k}=0.00005$')
plt.xlabel("n")
plt.ylabel("f(x)")
plt.legend()
plt.savefig("subgradient100000.jpg")
plt.show()
