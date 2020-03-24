import requests
from bs4 import BeautifulSoup
import re
import traceback
import smtplib
from email.mime.text import MIMEText
from smtplib import SMTP_SSL

def getHTMLtext(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except Exception as e:
        traceback.format_exc()


def htmlparser(text):
    soup=BeautifulSoup(text, 'html.parser')
    weatherspantag1=soup.find_all('h1')[1]
    weatherspantag2=soup.find_all('h1')[2]
    weatherspanname1=weatherspantag1.string
    weatherspanname2 = weatherspantag2.string
    weathertag1=weatherspantag1.parent
    weathertag2 = weatherspantag2.parent
    weatherattributetag1=weathertag1.find('p', attrs={'class': 'wea'})
    weatherattributetag2=weathertag2.find('p', attrs={'class': 'wea'})
    weatherattribute1=weatherattributetag1.string
    weatherattribute2 = weatherattributetag2.string
    weathertemtag1=weathertag1.find('p', attrs={'class': 'tem'})
    weathertemtag2 = weathertag2.find('p', attrs={'class': 'tem'})
    weathertem1=weathertemtag1.find('span').string
    weathertem2 = weathertemtag2.find('span').string
    clothtags=soup.find_all('em')
    cloth=None
    for i in clothtags:
        if i.string=='穿衣指数':
            cloth=i.parent.find('p').string
            break
    content1=weatherspanname1+':'+weatherattribute1+','+weathertem1+'℃'
    content2 = weatherspanname2 + ':' + weatherattribute2 + ',' + weathertem2 + '℃'
    content3 = '穿衣指数:'+cloth
    content=content1+'\n'+content2+'\n'+content3
    titletag=soup.find('input',attrs={'id':"hidden_title"})
    title=titletag.attrs['value']
    regex=re.compile(r'.雨')
    result=re.findall(regex,title)
    if result:
        results=''
        for i in range(len(result)):
            results=results+result[i]
        title='今天有'+results+', 笨猪要记得带伞'
    return title,content


def send_mail(username, passwd, recv, title, content, mail_host='smtp.qq.com', port=465):
    msg = MIMEText(content)
    msg['Subject'] = title
    msg['From'] = username
    msg['To'] = recv
    print('Begin Connect...')
    smtp = SMTP_SSL(mail_host, port=port)
    print('Begin Login...')
    smtp.login(username, passwd)
    print('Begin Send...')
    smtp.sendmail(username, recv, msg.as_string())
    smtp.quit()
    print('email send success.')


url="http://www.weather.com.cn/weather1d/101250109.shtml"
text=getHTMLtext(url)
title,content=htmlparser(text)
email_user = '1572808459@qq.com'
email_pwd = 'txmeskvtpydujgij'
maillist = '1572808459@qq.com'
send_mail(email_user, email_pwd, maillist, title, content)