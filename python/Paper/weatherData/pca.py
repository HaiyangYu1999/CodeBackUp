#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def PCA(dataArray):
    dataArray=dataArray.T
    corr=np.corrcoef(dataArray)
    (A,B)=np.linalg.eig(corr)
    return A,B


def showPic(dataArray):
    A, B = PCA(dataArray)
    ratio = 0
    for i in range(len(A)):
        ratio += A[i] / sum(A)
        print(round(ratio, 5))
    x = []
    for i in range(1, 21):
        x.append(i)
    plt.xticks(x)
    plt.plot(x, A, color='black', marker='o')
    plt.xlim(1, 20)
    plt.ylim(0, 8)
    plt.xlabel("Principal Component Number")
    plt.ylabel("Eigenvalue")
    plt.title("Variance Ratio")
    plt.show()


if __name__=="__main__":
    a=np.loadtxt('MonthlyWeather.txt',delimiter=',')
    A, B = PCA(a)
    showPic(a)
    P=B[0:7]
    C=np.dot(P,a.T)
    np.savetxt('dataAfterPCA.txt',C,delimiter=' ')

