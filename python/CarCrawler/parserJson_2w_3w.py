import json
import csv

## 由makeHeader.py生成表头
HEADER = ['specid', '车型名称', '厂商指导价(元)', '厂商', '级别', '能源类型', '环保标准', '上市时间', '最大功率(kW)',
          '最大扭矩(N·m)', '发动机', '变速箱', '长*宽*高(mm)', '车身结构', '最高车速(km/h)', '官方0-100km/h加速(s)',
          '实测0-100km/h加速(s)', '实测100-0km/h制动(m)', '工信部综合油耗(L/100km)', '实测油耗(L/100km)', '整车质保',
          '长度(mm)', '宽度(mm)', '高度(mm)', '轴距(mm)', '前轮距(mm)', '后轮距(mm)', '最小离地间隙(mm)', '车身结构',
          '车门数(个)', '座位数(个)', '油箱容积(L)', '行李厢容积(L)', '整备质量(kg)', '发动机型号', '排量(mL)', '进气形式',
          '气缸排列形式', '气缸数(个)', '每缸气门数(个)', '压缩比', '配气机构', '缸径(mm)', '行程(mm)', '最大马力(Ps)',
          '最大功率(kW)', '最大功率转速(rpm)', '最大扭矩(N·m)', '最大扭矩转速(rpm)', '发动机特有技术', '燃料形式', '燃油标号',
          '供油方式', '缸盖材料', '缸体材料', '环保标准', '挡位个数', '变速箱类型', '简称', '驱动方式', '前悬架类型', '后悬架类型',
          '助力类型', '车体结构', '前制动器类型', '后制动器类型', '驻车制动类型', '前轮胎规格', '后轮胎规格', '备胎规格',
          '主/副驾驶座安全气囊', '前/后排侧气囊', '前/后排头部气囊(气帘)', '膝部气囊', '后排安全带式气囊', '后排中央安全气囊',
          '被动行人保护', '缺气保用轮胎', 'ISOFIX儿童座椅接口', 'ABS防抱死', '制动力分配(EBD/CBC等)', '刹车辅助(EBA/BAS/BA等)',
          '牵引力控制(ASR/TCS/TRC等)', '车身稳定控制(ESC/ESP/DSC等)', '并线辅助', '车道偏离预警系统', '车道保持辅助系统',
          '道路交通标识识别', '主动刹车/主动安全系统', '夜视系统', '疲劳驾驶提示', '前/后驻车雷达', '倒车车侧预警系统',
          '自动泊车入位', '发动机启停技术', '自动驻车', '上坡辅助', '陡坡缓降', '空气悬架', '电磁感应悬架', '可变转向比',
          '中央差速器锁止功能', '整体主动转向系统', '涉水感应系统', '运动外观套件', '电动后备厢', '感应后备厢', '电动后备厢位置记忆',
          '尾门玻璃独立开启', '车顶行李架', '发动机电子防盗', '车内中控锁', '无钥匙启动系统', '主动闭合式进气格栅', '电池预加热',
          '多功能方向盘', '方向盘换挡', '方向盘加热', '方向盘记忆', '全液晶仪表盘', 'HUD抬头数字显示', '内置行车记录仪', '主动降噪',
          '电动可调踏板', '运动风格座椅', '主/副驾驶座电动调节', '副驾驶位后排可调节按钮', '后排座椅电动调节', '后排小桌板',
          '第二排独立座椅', '后排座椅电动放倒', '前/后中央扶手', '后排杯架', 'GPS导航系统', '导航路况信息显示', '道路救援呼叫',
          '中控液晶屏分屏显示', '蓝牙/车载电话', '手势控制', '车联网', 'OTA升级', '车载电视', '后排控制多媒体', '220V/230V电源',
          '行李厢12V电源接口', 'LED日间行车灯', '自适应远近光', '自动头灯', '转向辅助灯', '转向头灯', '前大灯雨雾模式', '大灯高度可调',
          '大灯清洗装置', '大灯延时关闭', '触摸式阅读灯', '前/后电动车窗', '车窗防夹手功能', '后风挡遮阳帘', '后排侧隐私玻璃', '后雨刷',
          '可加热喷水嘴', '后排独立空调', '后座出风口', '温度分区控制', '车载空气净化器', '车内PM2.5过滤装置', '负离子发生器',
          '车内香氛装置', '车载冰箱']

lists = []
lists.append(HEADER)
with open("20000-30000.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if i % 100 == 0:
            print("begin to parser {}-th file, {} files in total".format(i, len(lines)))
        data = json.loads(lines[i])

        try:
            list = []

            dataParam = data["param"]

            dataParam0 = dataParam[0]["paramitems"]  # 基本参数
            specid = dataParam0[0]["valueitems"][0]["specid"]
            list.append(specid)
            for i in range(len(dataParam0)):
                if i == 5 and dataParam0[i]["name"] != "环保标准":
                    list.append("NULL")
                if i == 6 and dataParam0[i]["name"] != "上市时间":
                    list.append("NULL")
                list.append(dataParam0[i]["valueitems"][0]["value"])

            dataParam1 = dataParam[1]["paramitems"]  # 车身
            for i in dataParam1:
                list.append(i["valueitems"][0]["value"])

            dataParam2 = dataParam[2]["paramitems"]  # 发动机
            for i in dataParam2:
                list.append(i["valueitems"][0]["value"])

            dataParam3 = dataParam[3]["paramitems"]  # 变速箱
            for i in dataParam3:
                list.append(i["valueitems"][0]["value"])

            dataParam4 = dataParam[4]["paramitems"]  # 底盘转向
            for i in dataParam4:
                list.append(i["valueitems"][0]["value"])

            dataParam5 = dataParam[5]["paramitems"]  # 车轮制动
            for i in dataParam5:
                list.append(i["valueitems"][0]["value"])

            dataConfig = data["config"]

            dataConfig0 = dataConfig[0]["configitems"]  # 主/被动安全装备
            for i in dataConfig0:
                list.append(i["valueitems"][0]["value"])

            dataConfig1 = dataConfig[1]["configitems"]  # 辅助/操控配置
            for i in dataConfig1:
                list.append(i["valueitems"][0]["value"])

            dataConfig2 = dataConfig[2]["configitems"]  # 外部/防盗配置
            for i in dataConfig2:
                list.append(i["valueitems"][0]["value"])

            dataConfig3 = dataConfig[3]["configitems"]  # 内部配置
            for i in dataConfig3:
                list.append(i["valueitems"][0]["value"])

            dataConfig4 = dataConfig[4]["configitems"]  # 座椅配置
            for i in dataConfig4:
                list.append(i["valueitems"][0]["value"])

            dataConfig5 = dataConfig[5]["configitems"]  # 多媒体配置
            for i in dataConfig5:
                list.append(i["valueitems"][0]["value"])

            dataConfig6 = dataConfig[6]["configitems"]  # 灯光配置
            for i in dataConfig6:
                list.append(i["valueitems"][0]["value"])

            dataConfig7 = dataConfig[7]["configitems"]  # 玻璃/后视镜
            for i in dataConfig7:
                list.append(i["valueitems"][0]["value"])

            dataConfig8 = dataConfig[8]["configitems"]  # 空调/冰箱
            for i in dataConfig8:
                list.append(i["valueitems"][0]["value"])

            lists.append(list)
        except Exception as e:
            pass
        finally:
            pass

    print('-------------------------------------------------------------')
    print("begin to write Files")
    with open("20000-30000.csv", 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for i in lists:
            writer.writerow(i)
    print("finished writing Files")