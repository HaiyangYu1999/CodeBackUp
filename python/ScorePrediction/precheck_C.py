#!/usr/bin/env python3
import pandas as pd
import numpy as np
import statsmodels.tsa.stattools as ts
from statsmodels.sandbox.stats.diagnostic import acorr_ljungbox


if __name__ == "__main__":
    allData=pd.read_csv('score.csv',header=None,sep=',')
    for i in range(np.size(allData,1)):
        data = allData.iloc[:, i]
        print(ts.adfuller(data,autolag='AIC'))
        qljungbox, pval, qboxpierce, pvalbp = acorr_ljungbox(data, boxpierce=True,lags=[24,6])
        print(pval)