import re
import requests


def getHTMLtext(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print(e)


def htmlparser(text):
    try:
        match1 = re.findall(r'target="_blank" title=".*"', text)
        match2 = re.findall(r'em title="[\d\.]*"', text)
        ulist=[]
        if len(match1) == len(match2):
            for i in range(len(match1)):
                m1=(match2[i].split('=')[1])
                m11=m1.split('"')[1]
                m2 =(match1[i].split('=')[2])
                m22=m2.split('"')[1]
                if m22=="":
                    continue
                ulist.append([m11,m22])

        else:
            print('reenter the regular expression')
        return ulist
    except:
        raise


def printlist(ulist):
    print('{:5}\t{:10}\t{:10}'.format('序号','价格','名称'))
    for i in range(len(ulist)):
        print('{:5}\t{:10}\t{:10}'.format(i+1,ulist[i][0],ulist[i][1]))

url="https://list.tmall.com/search_product.htm?q=围巾"

text=getHTMLtext(url)
ulist=htmlparser(text)
printlist(ulist)