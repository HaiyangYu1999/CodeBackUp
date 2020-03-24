import requests
from bs4 import BeautifulSoup
import re
import time
import pymysql


def getHTMLText(url):
    try:
        r = requests.get(url,timeout=5)
        r.raise_for_status()
        r.encoding ='gbk'
        return r.text
    except Exception as e:
        pass


def getStockList(text):
    lst=[]
    soup = BeautifulSoup(text, 'html.parser')
    a = soup.find_all('a', attrs={"target":"_blank"})
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue
    return lst


def getStockData(url):
    datalist=[]
    with open('./stocklist.txt','r') as f:
        list=f.readlines()
    for s in list:
        s=s.strip('\n')
        urlnow=url+s
        k=0
        data=getHTMLText(urlnow)
        while(data==None and k<10):
            data = getHTMLText(urlnow)
            k=k+1
        if k==10:
            continue
        data = data.split("=")[1]
        data = data[:-2]
        data = data.strip('\"')
        if data=="":
            continue
        print(data)
        datalist.append(data)
    return datalist


def datasaveSQL(url):
    with open('./stocklist.txt','r') as f:
        list=f.readlines()
    db = pymysql.connect("localhost", "root", "mm19990126", "test")
    cursor = db.cursor()
    for s in list:
        s=s.strip('\n')
        urlnow=url+s
        k=0
        data=getHTMLText(urlnow)
        while(data==None and k<10):
            data = getHTMLText(urlnow)
            k=k+1
        if k==10:
            continue
        data = data.split("=")[1]
        data = data[:-2]
        data = data.strip('\"')
        if data=="":
            continue
        dlist=data.split(',')
        sql = "INSERT INTO test(name, code) VALUES ('%s', '%s' )" % (dlist[0],s)
        #print(data)
        cursor.execute(sql)
    db.commit()
    db.close()


def savelist(lst):
    with open(r'./stocklist.txt','w') as f:
        for i in range(len(lst)):
            f.write(lst[i]+'\n')


url_list= 'http://quote.eastmoney.com/stocklist.html'
url="https://hq.sinajs.cn/list="
print(time.asctime( time.localtime(time.time()) ))
#datalist=getStockData(url)
datasaveSQL(url)
print(time.asctime( time.localtime(time.time()) ))
