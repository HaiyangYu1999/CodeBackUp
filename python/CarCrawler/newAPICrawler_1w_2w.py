import requests
import json

with open("10000-20000.txt", 'w', encoding='utf-8') as f:
    for i in range(10000, 20000):
        url = "https://car.m.autohome.com.cn/ashx/car/GetModelConfig.ashx?ids={}".format(i)
        try:
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            r = requests.get(url, timeout=5)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
        except Exception as e:
            pass
        finally:
            pass
        text = r.text
        data = json.loads(text)
        if data["param"] == None:
            if i % 10 == 0:
                print(i)
        else:
            f.write(text)
            f.write("\n")