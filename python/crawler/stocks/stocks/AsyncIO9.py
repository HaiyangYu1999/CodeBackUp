import asyncio
import aiohttp
import pymysql
import time


async def getpage(s):
    try:
        url = "https://hq.sinajs.cn/list="
        s = s.strip('\n')
        urlnow=url+s
        async with aiohttp.request('GET',urlnow) as r:
            res = await r.text(encoding='gbk')
        data=res
        k=0
        while data==None and k<10:
            async with aiohttp.request('GET', urlnow) as r:
                res = await r.text(encoding='gbk')
            data = res
        data = data.split("=")[1]
        if data!="":
            data = data[:-2]
            data = data.strip('\"')
            data = data.split(',')
            #print(data)
            singleinsert(data)
    except:
        pass


def singleinsert(data):
    if data!=['']:
        dlist = data
        sql = "INSERT INTO stocktest2(name, jinkai, zuoshou,max,min,volume,turn_volume,date) \
                VALUES ('%s', '%f', '%f', '%f','%f','%f','%f','%s' )" % (
        dlist[0], float(dlist[1]), float(dlist[2]), float(dlist[4]), float(dlist[5]), float(dlist[8]), float(dlist[9]),
        dlist[-3])
        cursor.execute(sql)


def runEventLoop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(getpage(s))
    loop.close()




if __name__=='__main__':
    print(time.asctime(time.localtime(time.time())))
    tasks = []
    with open(r'./stocklist.txt', 'r') as f:
        slist = f.readlines()
    db = pymysql.connect("localhost", "root", "mm19990126", "test")
    cursor = db.cursor()
    for s in slist[4000:4499]:
        tasks.append(asyncio.ensure_future(getpage(s)))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    tasks = []
    db.commit()
    db.close()
    print(time.asctime(time.localtime(time.time())))

