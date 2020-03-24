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
        match1 = re.findall(r'<a href=".*?data-p=".*-11" >.*?<', text)
        match2 = re.findall(r'<em title="[\d\.]*"><b>', text)
        match3 = re.findall(r'<span>该款月成交 <em>.*?</em></span>',text)
        ulist=[]
        if len(match1)==len(match2):
            for i in range(len(match1)):
                m1=(match1[i].split('data-p=')[1])
                m11=m1.split('>')[1]
                m111=m11.split('<')[0]
                m2 =(match2[i].split('"')[1])
                m3 = (match3[i].split('<em>')[1])
                m33 = m3.split('</em>')[0]
                if m2=="":
                    continue
                ulist.append([m111,m2,m33])

        else:
            print('reenter the regular expression')
        return ulist
    except:
        raise


def printlist(ulist):
    print('{:5}\t{:10}\t{:10}\t{:10}'.format('序号','价格','月成交量','名称'))
    for i in range(len(ulist)):
        print('{:5}\t{:10}\t{:10}\t{:10}'.format(i+1,ulist[i][1],ulist[i][2],ulist[i][0]))

url="https://list.tmall.com/search_product.htm?q=口红"

text=getHTMLtext(url)
ulist=htmlparser(text)
printlist(ulist)