import requests
from bs4 import BeautifulSoup
import traceback
import re
import time


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
        print(len(list))
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


def savelist(lst):
    with open(r'./stocklist.txt','w') as f:
        for i in range(len(lst)):
            f.write(lst[i]+'\n')


url_list= 'http://quote.eastmoney.com/stocklist.html'
url="https://hq.sinajs.cn/?_=0.24204334984696851&list="
print(time.asctime( time.localtime(time.time()) ))
url_test="https://hq.sinajs.cn/?_=0.24204334984696851&list="
lst_test=['sh501061']
datalist=getStockData(url)
print(time.asctime( time.localtime(time.time()) ))
url1=url_test+lst_test[0]
print(len(datalist))