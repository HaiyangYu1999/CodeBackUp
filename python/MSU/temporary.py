import numpy as np
import pandas as pd
import tensorflow as tf


data=pd.read_csv("Data1(20%).csv")
print(data.head())

model=tf.keras.Sequential(
    [tf.keras.layers.Dense(10,input_shape=(5,),activation='relu'),
     tf.keras.layers.Dense(1)]
)
model.compile(optimizer='adam',loss='mse')
x=data.iloc[:,:-1]
y=data.iloc[:,-1]
model.fit(x,y,epochs=1000)
test=data.iloc[:10,:-1]
print(model.predict(test))
print(data.iloc[:10,-1])