import requests
from bs4 import BeautifulSoup
import traceback
import os


def getHTMLtext(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except Exception as e:
        traceback.format_exc()


def htmlparser(text):
    ulist1=[]
    ulist2=[]
    ulist=[ulist1,ulist2]
    soup=BeautifulSoup(text,'html.parser')
    goodstag=soup.find_all('strong',attrs={'data-done':"1"})
    goodnametag=soup.find_all('div',attrs={'class':'p-name p-name-type-2'})
    for i in goodstag:
        m1=i.find('i').string
        ulist1.append(m1)
    for j in goodnametag:
        try:

            m2=j.find('a').find('em').get_text()
            ulist2.append(m2)
        except:
            continue
    if len(ulist1)!=len(ulist2):
        print('counts error')
    return ulist


def output(ulist,path,nowpage,depth):
    with open(path,'a') as f:
        for i in range(len(ulist[0])):
            try:
                f.write(ulist[0][i])
                f.write('\t')
                f.write(ulist[1][i])
                f.write('\n')
            except:
                continue

def main(goods,depth=3):
    for i in range(depth):
        url="https://search.jd.com/Search?keyword="+goods+"&enc=utf-8&page="+str(2*i-1)
        path=r'./JDsearch/'
        if not os.path.exists(path):
            os.makedirs(path)
        path=path+goods+'.txt'
        text=getHTMLtext(url)
        ulist=htmlparser(text)
        output(ulist,path,nowpage=i,depth=depth)
    pass
main('送男友')

