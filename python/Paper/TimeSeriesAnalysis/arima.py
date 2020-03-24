#!/usr/bin/env python3
import pandas as pd
import numpy as np
import statsmodels.tsa.stattools as st
from statsmodels.tsa.arima_model import ARMA
from statsmodels.sandbox.stats.diagnostic import acorr_ljungbox
import matplotlib.pyplot as plt

if __name__ == "__main__":
    allData=pd.read_csv('MonthlyWeather.txt',header=None,sep=',')
    data=allData.iloc[:,0]
    original_new=data[234:]
    data=data[0:234]
    order = st.arma_order_select_ic(data,ic=['aic', 'bic'])
    model = ARMA(data, order=(4,3))
    result_arma = model.fit(disp=-1,method='css')
    print(result_arma.summary())
    predict_ts = result_arma.predict()
    err=(data-predict_ts).dropna()
    p_value = acorr_ljungbox(err,[6,12,18,24])
    print(p_value)
    predict_new=result_arma.predict(234,271,)
    ax=predict_new.plot(label='forecast')
    original_new.plot(label='observed')
    ax.set_xlabel('Month')
    ax.set_ylabel('Precipitation')
    plt.legend()
    plt.show()
    predict_new=predict_new.values
    original_new=original_new.values
    tp=0
    tn=0
    fp=0
    fn=0
    threshold=3.94
    P=R=F1=0
    for i in range(np.size(predict_new)):
        if predict_new[i]<3 and original_new[i]<3:
            tp+=1
        if predict_new[i]<3 and original_new[i]>3:
            fp+=1
        if predict_new[i]>3 and original_new[i]<3:
            fn+=1
        if predict_new[i]>3 and original_new[i]>3:
            tn+=1
    P=tp/(tp+fp)
    R=tp/(tp+fn)
    F1=2*P*R/(P+R)
    print('P=',P,',R=',R,',F1=',F1)