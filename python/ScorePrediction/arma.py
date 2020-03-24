#!/usr/bin/env python3
import pandas as pd
import statsmodels.api as sm
import numpy as np
import statsmodels.tsa.stattools as st
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima_model import ARMA
from statsmodels.sandbox.stats.diagnostic import acorr_ljungbox
import matplotlib.pyplot as plt

if __name__=="__main__":
    allData=pd.read_csv('score.csv',header=None,sep=',')
    predict = []
    for i in range(16):
        data=allData.iloc[:,i]
        order = st.arma_order_select_ic(data,ic=['aic', 'bic'])
        print(order)
        fig = plt.figure(figsize=(12, 8))
        ax1 = fig.add_subplot(211)
        fig = sm.graphics.tsa.plot_acf(data, lags=40, ax=ax1)
        ax2 = fig.add_subplot(212)
        fig = sm.graphics.tsa.plot_pacf(data, lags=40, ax=ax2)
        plt.savefig("ARMA1_{}.png".format(i))
        plt.show()
        arma_mod20 = sm.tsa.ARMA(data, (8, 0)).fit()
        print(arma_mod20.aic, arma_mod20.bic, arma_mod20.hqic) #414.23057435245903 440.282276212 424.774166869
        arma_mod30 = sm.tsa.ARMA(data, (0, 1)).fit()
        print(arma_mod30.aic, arma_mod30.bic, arma_mod30.hqic)#409.9068558490347 417.722366407 413.069933604
        arma_mod40 = sm.tsa.ARMA(data, (8, 1)).fit()
        print(arma_mod40.aic, arma_mod40.bic, arma_mod40.hqic)#420.09288437102913 448.749756417 431.690836139
        arma_mod50 = sm.tsa.ARMA(data, (9, 0)).fit()
        print(arma_mod50.aic, arma_mod50.bic, arma_mod50.hqic)#415.5112511748553 444.168123221 427.109202943
        fig = plt.figure(figsize=(12, 8))
        model = ARMA(data, order=(8, 4))
        result_arma = model.fit(disp=-1, method='css')
        predict_new = result_arma.predict(10,100)
        print(np.size(predict_new))
        original_new=data[9:100]
        print(np.size(original_new))
        err = (data - predict_new).dropna()
        p_value = acorr_ljungbox(err, [12, 6])
        print(p_value)
        ax = predict_new.plot(label='forecast')
        original_new.plot(label='observed')
        ax.set_xlabel('Time')
        ax.set_ylabel('Scores')
        plt.legend()
        plt.savefig("ARMA2_{}.png".format(i))
        predict.append(predict_new.values[-1])
    print(predict)
