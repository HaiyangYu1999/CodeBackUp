import requests
import os
url="http://m.ip138.com/ip.asp"
kv={'ip':'202.204.80.112'}
try:
    r=requests.get(url,params=kv)
    r.raise_for_status()
except Exception as e:
    print(e)
else:
    print(r.text)