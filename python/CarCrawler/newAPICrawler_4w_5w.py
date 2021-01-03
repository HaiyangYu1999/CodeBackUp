import requests
import json

with open("40000-50000.txt", 'w', encoding='utf-8') as f:
    for i in range(40000, 50000):
        try:
            url = "https://car.m.autohome.com.cn/ashx/car/GetModelConfig.ashx?ids={}".format(i)
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            r = requests.get(url, timeout=5)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            text = r.text
            data = json.loads(text)
        except Exception as e:
            pass
        finally:
            pass
        if data["param"] == None:
            if i % 100 == 0:
                print(i)
        else:
            f.write(text)
            f.write("\n")