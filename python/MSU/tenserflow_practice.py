import numpy as np
import pandas as pd
import random

data = pd.read_csv("./imputation/data{}_{}-{}.csv".format(1,"HD",20))
s=range(50)
smpl = random.sample(s, 5)

d=data.iloc[smpl,:]
print(smpl)
sSet=set(s)
smplSet=set(smpl)
testSet=sSet-smplSet
test=list(testSet)
