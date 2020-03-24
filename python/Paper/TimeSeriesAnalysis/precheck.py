#!/usr/bin/env python3
import pandas as pd
import statsmodels.tsa.stattools as ts
from statsmodels.sandbox.stats.diagnostic import acorr_ljungbox

if __name__=="__main__":
    allData=pd.read_csv('MonthlyWeather.txt',header=None,sep=',')
    data=allData.iloc[:,0]
    print(ts.adfuller(data,autolag='AIC'))
    p_value = acorr_ljungbox(data,lags=[6,12])
    print(p_value)