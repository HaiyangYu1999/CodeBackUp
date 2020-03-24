import numpy as np
import matplotlib.pyplot as plt

eps=1e-2      #P(|X1+...+Xn-EX1-...-EXn|>=eps)<sigma/(n*eps^2)
error=0.01
n=round(1/(error*eps**2))
y=[]
for i in range(1,21):
    X=np.random.randn(n,i)
    Y=np.amax(X,axis=1)
    Ey=np.mean(Y)
    y.append(Ey)

x=list(range(1,21))
fig, ax=plt.subplots(figsize=(10,10))
ax.plot(x,y)
plt.xlabel("n")
plt.ylabel("EYn")
plt.savefig("STT886HW3.jpg")
plt.show()