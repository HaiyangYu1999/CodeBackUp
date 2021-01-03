import json

maxlen = 0

maxlist = 0

maxindex = 0
with open("data.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for k in range(len(lines)):
        try:
            data = json.loads(lines[k])
            list = []
            list.append("specid")
            dataParam = data["param"]

            dataParam0 = dataParam[0]["paramitems"] #基本参数
            for i in dataParam0:
                list.append(i["name"])

            dataParam1 = dataParam[1]["paramitems"] #车身
            for i in dataParam1:
                list.append(i["name"])

            dataParam2 = dataParam[2]["paramitems"] #发动机
            for i in dataParam2:
                list.append(i["name"])

            dataParam3 = dataParam[3]["paramitems"]  # 变速箱
            for i in dataParam3:
                list.append(i["name"])

            dataParam4 = dataParam[4]["paramitems"]  # 底盘转向
            for i in dataParam4:
                list.append(i["name"])

            dataParam5 = dataParam[5]["paramitems"]  # 车轮制动
            for i in dataParam5:
                list.append(i["name"])

            dataParam6 = dataParam[6]["paramitems"]  # 车轮制动
            for i in dataParam6:
                list.append(i["name"])

            dataConfig = data["config"]

            dataConfig0 = dataConfig[0]["configitems"]  #  主/被动安全装备
            for i in dataConfig0:
                list.append(i["name"])

            dataConfig1 = dataConfig[1]["configitems"]  # 辅助/操控配置
            for i in dataConfig1:
                list.append(i["name"])

            dataConfig2 = dataConfig[2]["configitems"]  # 外部/防盗配置
            for i in dataConfig2:
                list.append(i["name"])

            dataConfig3 = dataConfig[3]["configitems"]  # 内部配置
            for i in dataConfig3:
                list.append(i["name"])

            dataConfig4 = dataConfig[4]["configitems"]  # 座椅配置
            for i in dataConfig4:
                list.append(i["name"])

            dataConfig5 = dataConfig[5]["configitems"]  # 多媒体配置
            for i in dataConfig5:
                list.append(i["name"])

            dataConfig6 = dataConfig[6]["configitems"]  # 灯光配置
            for i in dataConfig6:
                list.append(i["name"])

            dataConfig7 = dataConfig[7]["configitems"]  # 玻璃/后视镜
            for i in dataConfig7:
                list.append(i["name"])

            dataConfig8 = dataConfig[8]["configitems"]  # 空调/冰箱
            for i in dataConfig8:
                list.append(i["name"])


            if len(list) >= maxlen:
                maxlen = len(list)
                maxlist = list
                maxindex = lines[k]
        except Exception as e:
            pass
        finally:
            pass

    print(maxindex)
    print(maxlist)
    print(maxlen)
