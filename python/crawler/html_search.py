import requests
from bs4 import BeautifulSoup
import re

url="http://python123.io/ws/demo.html"
r=requests.get(url)
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
s=soup.find_all()
print(type(s))
