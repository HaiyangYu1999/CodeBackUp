import requests
import os

url="https://gss0.baidu.com/9fo3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/a9d3fd1f4134970a62307da79ecad1c8a6865df2.jpg"
name=url.split('/')[-1]
try:
    r=requests.get(url)
    r.raise_for_status()
except Exception as e:
    print(e)
root="F:/materials/python projects/picture/"
path=root+name


if not os.path.exists(root):
    os.mkdir(root)
if not os.path.exists(path):
    with open(path,'wb') as f:
        f.write(r.content)
        f.close()
        print('saved successfully')
else:
    print('the file has already existed!')

