import requests
import json

with open("0-10000.txt", 'w', encoding='utf-8') as f:
    for i in range(0, 10000):
        url = "https://car.m.autohome.com.cn/ashx/car/GetModelConfig.ashx?ids={}".format(i)
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        try:
            r = requests.get(url, timeout=5)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
        except Exception as e:
            pass
        finally:
            pass
        text = r.text
        data = json.loads(text)
        if i % 100 == 0:
            print(i)
        if data["param"] == None:
            pass
        else:
            f.write(text)
            f.write("\n")