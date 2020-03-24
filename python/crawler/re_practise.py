from bs4 import BeautifulSoup
import requests
import re

url="https://search.jd.com/Search?keyword=手机&enc=utf-8&page=1"
r=requests.get(url)
r.encoding=r.apparent_encoding
soup=BeautifulSoup(r.text,'html.parser')
a=soup.find_all