import pymysql
from sklearn import linear_model
import numpy
import time
import multiprocessing


def datasearch(code,cursor):
    sql="SELECT * FROM test WHERE code='%s';" % (code)
    cursor.execute(sql)
    name=cursor.fetchone()
    print(name)
    if name==None:
        return []
    name=name[0]
    data=[]
    for i in stockdate:
        sqlsearch="SELECT * FROM %s WHERE name='%s';" % (i,name)
        cursor.execute(sqlsearch)
        data.append(cursor.fetchone())
    if len(data)<11:
        data=[]
    return data


def linear_model_main(Xlist, Ylist):
    regr = linear_model.LinearRegression()
    regr.fit(Xlist, Ylist)
    return regr.coef_, regr.intercept_



def predict(data):
    outcome=[]
    outcome.append(data[0][0])
    for i in range(1,7):
        y=[]
        for s in range(len(stockdate)):
            y.append(float(data[s][i]))
        y1=numpy.array(y)
        intarray=numpy.array(intdate)
        a,b=linear_model_main(intarray.reshape(-1,1),y1.reshape(-1,1))
        pre1=a*17+b
        pre1=float(pre1)
        outcome.append(pre1)
    outcome.append('2018-11-17_predict')
    return outcome


def singleinsert(data):
    dlist = data
    sql = "INSERT INTO multiprocess(name, jinkai, zuoshou,max,min,volume,turn_volume,date) \
            VALUES ('%s', '%.2f', '%.2f', '%.2f','%.2f','%.2f','%.2f','%s' )" % (
    dlist[0], float(dlist[1]), float(dlist[2]), float(dlist[3]), float(dlist[4]), float(dlist[5]), float(dlist[6]),
    dlist[7])
    cursor.execute(sql)


def whole(code):
        data=datasearch(code)
        if data==[]:
            return ''
        outcome=predict(data)
        #singleinsert(outcome)


def fun(i):
    print(i)

if __name__=='__main__':
    print(time.asctime( time.localtime(time.time()) ))
    date = ['02', '05', '06', '07', '08', '09', '12', '13', '14', '15', '16']
    stockdate=[]
    intdate=[]
    for i in date:
        stockdate.append('stock11'+i)
        intdate.append(int(i))
    with open(r'./stocklist.txt', 'r') as f:
        slist = f.readlines()
    db = pymysql.connect("localhost", "root", "mm19990126", "test")
    cursor = db.cursor()
    pool = multiprocessing.Pool()
    for s in slist:
        i = s.strip('\n')
        pool.apply_async(datasearch, args=(i,cursor))
    pool.close()
    pool.join()
    db.commit()
    db.close()

    print(time.asctime( time.localtime(time.time())))
