#!/usr/bin/env python3
import csv
import numpy as np


if __name__=="__main__":
    data=[]
    with open('MonthlyWeather.csv','r') as f:
        file=csv.reader(f)
        for i in file:
            data.append(i)
    m=np.size(data,0)
    n=np.size(data,1)
    precipitation=[]
    for i in range(1,m):
        precipitation.append(float(data[i][1]))
    precipitation=precipitation[1:]
    a=np.loadtxt('dataAfterPCA.txt')
    b=np.delete(a,271,axis=1)
    b=np.row_stack((b,precipitation))
    np.savetxt('dataPlusPrecipitation.txt',b)
