import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import integrate
mu=0
sigma=1
pi=2*math.acos(0)

def px(x):
    return 1/(math.sqrt(2*pi*sigma))*math.exp(-((x-mu)**2)/(2*sigma**2))

def Fx(x):
    res = integrate.quad(px,-np.inf,x)
    return res[0]

y=[]
for i in range(1,21):
    ypy=lambda y:y*i*px(y)*Fx(y)**(i-1)
    res=integrate.quad(ypy,-np.inf,np.inf)[0]
    y.append(res)

x=list(range(1,21))
fig, ax=plt.subplots(figsize=(10,10))
ax.plot(x,y,color='g')
plt.xlabel("n")
plt.ylabel("E(Yn)")
plt.savefig("STT886HomeWork3.jpg")
plt.show()
