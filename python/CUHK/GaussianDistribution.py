import pandas as pd
import numpy as np
import csv

data=pd.read_csv('discrete.csv',header=None,sep=',')
size=50
gmat=data.iloc[:,2]
gmat_mean=gmat.mean()
gmat_std=gmat.std()
gmat_n=np.random.randn(1,size)[0]
gmat_random=gmat_n*gmat_std+gmat_mean
gmat_random=gmat_random.T
gpa=data.iloc[:,3]
gpa_mean=gpa.mean()
gpa_std=gpa.std()
gpa_n=np.random.randn(1,size)[0]
gpa_random=gpa_n*gpa_std+gpa_mean
gpa_random=gpa_random.T
rank_random=np.random.randint(1,5,size)
rank_random=rank_random.T
random=np.zeros((size,3))
for i in range(size):
    gpa1=np.random.randn(1,1)[0][0]*gpa_std+gpa_mean
    while gpa1>4.0 or gpa1<2.0:
        gpa1 = np.random.randn(1, 1)[0][0] * gpa_std + gpa_mean
    random[i][1] = gpa1
    gmat1=np.random.randn(1,1)[0][0]*gmat_std+gmat_mean
    while gmat1>800 or gmat1<200:
        gmat1 = np.random.randn(1, 1)[0][0] * gmat_std + gmat_mean
    random[i][0]=gmat1
    random[i][2]=rank_random[i]
np.savetxt('random_data.txt',random)
#with open('random_data.csv', 'w',newline='') as f:
#    w = csv.writer(f)
#    for row in random:
#        w.writerows(random)
