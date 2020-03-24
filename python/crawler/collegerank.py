import requests
import os
from bs4 import BeautifulSoup
import bs4


def gethtmltext(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except Exception as e:
        print(e)


def fillunivlist(html):
    soup=BeautifulSoup(html,"html.parser")
    body=soup.find('tbody')
    ulist=[]
    for tr in body.children:
        if isinstance(tr,bs4.element.Tag):
            td=tr.find_all('td')
            ulist.append([td[0].string,td[1].string,td[2].string])
    return ulist


def printunivlist(ulist,num=200):
    print("{:^10}\t{:^10}\t{:^10}".format("排名","名称","总分"))
    for i in range(num):
        u=ulist[i]
        print("{:^10}\t{:^10}\t{:^10}".format(u[0],u[1],u[2]))
    pass

url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
text=gethtmltext(url)
ulist = fillunivlist(text)
printunivlist(ulist)
