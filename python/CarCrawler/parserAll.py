import json
import csv

nullDescriptor = 'NULL'  # 如果对应的属性不存在, 就用这个字符串代替. 可以手动配置想要的字符串

HEADER = ['specid', '车型名称', '厂商指导价(元)', '厂商', '级别', '能源类型', '环保标准', '上市时间', '工信部纯电续航里程(km)',
          '快充时间(小时)', '慢充时间(小时)', '快充电量百分比', '最大功率(kW)', '最大扭矩(N·m)', '发动机', '电动机(Ps)', '变速箱',
          '长*宽*高(mm)', '车身结构', '最高车速(km/h)', '官方0-100km/h加速(s)', '实测0-100km/h加速(s)', '实测100-0km/h制动(m)',
          '实测续航里程(km)', '实测快充时间(小时)', '实测慢充时间(小时)', '工信部综合油耗(L/100km)', '实测油耗(L/100km)', '整车质保',
          '长度(mm)', '宽度(mm)', '高度(mm)', '轴距(mm)', '前轮距(mm)', '后轮距(mm)', '最小离地间隙(mm)', '车身结构', '车门数(个)',
          '座位数(个)', '油箱容积(L)', '行李厢容积(L)', '整备质量(kg)', '发动机型号', '排量(mL)', '进气形式', '气缸排列形式', '气缸数(个)',
          '每缸气门数(个)', '压缩比', '配气机构', '缸径(mm)', '行程(mm)', '最大马力(Ps)', '最大功率(kW)', '最大功率转速(rpm)',
          '最大扭矩(N·m)', '最大扭矩转速(rpm)', '发动机特有技术', '燃料形式', '燃油标号', '供油方式', '缸盖材料', '缸体材料', '环保标准',
          '电机类型', '电动机总功率(kW)', '电动机总扭矩(N·m)', '前电动机最大功率(kW)', '前电动机最大扭矩(N·m)', '后电动机最大功率(kW)',
          '后电动机最大扭矩(N·m)', '系统综合功率(kW)', '系统综合扭矩(N·m)', '驱动电机数', '电机布局', '电池类型', '工信部纯电续航里程(km)',
          '电池能量(kWh)', '百公里耗电量(kWh/100km)', '电池组质保', '快充时间(小时)', '慢充时间(小时)', '快充电量(%)', '挡位个数',
          '变速箱类型', '简称', '驱动方式', '四驱形式', '中央差速器结构', '前悬架类型', '后悬架类型', '助力类型', '车体结构',
          '前制动器类型', '后制动器类型', '驻车制动类型', '前轮胎规格', '后轮胎规格', '备胎规格', '主/副驾驶座安全气囊', '前/后排侧气囊',
          '前/后排头部气囊(气帘)', '膝部气囊', '副驾驶座垫式气囊', '后排安全带式气囊', '后排座椅防下滑气囊', '后排中央安全气囊', '被动行人保护',
          '胎压监测功能', '缺气保用轮胎', '安全带未系提醒', 'ISOFIX儿童座椅接口', 'ABS防抱死', '制动力分配(EBD/CBC等)', '刹车辅助(EBA/BAS/BA等)',
          '牵引力控制(ASR/TCS/TRC等)', '车身稳定控制(ESC/ESP/DSC等)', '并线辅助', '车道偏离预警系统', '车道保持辅助系统', '道路交通标识识别',
          '主动刹车/主动安全系统', '夜视系统', '疲劳驾驶提示', '前/后驻车雷达', '驾驶辅助影像', '倒车车侧预警系统', '巡航系统', '驾驶模式切换',
          '自动泊车入位', '发动机启停技术', '自动驻车', '上坡辅助', '陡坡缓降', '可变悬架功能', '空气悬架', '电磁感应悬架', '可变转向比',
          '中央差速器锁止功能', '整体主动转向系统', '限滑差速器/差速锁', '涉水感应系统', '天窗类型', '运动外观套件', '电动扰流板', '轮圈材质',
          '电动吸合车门', '侧滑门形式', '电动后备厢', '感应后备厢', '电动后备厢位置记忆', '尾门玻璃独立开启', '车顶行李架', '发动机电子防盗',
          '车内中控锁', '钥匙类型', '无钥匙启动系统', '无钥匙进入功能', '主动闭合式进气格栅', '远程启动功能', '车侧脚踏板', '电池预加热',
          '方向盘材质', '方向盘位置调节', '多功能方向盘', '方向盘换挡', '方向盘加热', '方向盘记忆', '行车电脑显示屏幕', '全液晶仪表盘',
          '液晶仪表尺寸', 'HUD抬头数字显示', '内置行车记录仪', '主动降噪', '手机无线充电功能', '电动可调踏板', '座椅材质', '运动风格座椅',
          '主座椅调节方式', '副座椅调节方式', '主/副驾驶座电动调节', '前排座椅功能', '电动座椅记忆功能', '副驾驶位后排可调节按钮', '第二排座椅调节',
          '后排座椅电动调节', '后排座椅功能', '后排小桌板', '第二排独立座椅', '座椅布局', '后排座椅放倒形式', '后排座椅电动放倒', '前/后中央扶手',
          '后排杯架', '加热/制冷杯架', '中控彩色液晶屏幕', '中控液晶屏尺寸', 'GPS导航系统', '导航路况信息显示', '道路救援呼叫', '中控液晶屏分屏显示',
          '蓝牙/车载电话', '手机互联/映射', '语音识别控制系统', '手势控制', '面部识别', '车联网', 'OTA升级', '车载电视', '后排液晶屏幕',
          '后排控制多媒体', '多媒体/充电接口', 'USB/Type-C接口数量', '车载CD/DVD', '220V/230V电源', '行李厢12V电源接口', '扬声器品牌名称',
          '扬声器数量', '近光灯光源', '远光灯光源', '灯光特色功能', 'LED日间行车灯', '自适应远近光', '自动头灯', '转向辅助灯', '转向头灯',
          '车前雾灯', '前大灯雨雾模式', '大灯高度可调', '大灯清洗装置', '大灯延时关闭', '触摸式阅读灯', '车内环境氛围灯', '前/后电动车窗',
          '车窗一键升降功能', '车窗防夹手功能', '多层隔音玻璃', '外后视镜功能', '内后视镜功能', '后风挡遮阳帘', '后排侧窗遮阳帘', '后排侧隐私玻璃',
          '车内化妆镜', '后雨刷', '感应雨刷功能', '可加热喷水嘴', '空调温度控制方式', '后排独立空调', '后座出风口', '温度分区控制', '车载空气净化器',
          '车内PM2.5过滤装置', '负离子发生器', '车内香氛装置', '车载冰箱']


lists = [HEADER]

with open("data.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        data = json.loads(lines[i])              #把每一行的json对象解析为字典. 然后每个字典的键都是字符串, 可以用dataParam = data["param"]这种方法取出param对应的对象

        try:
            list = []

            dataParam = data["param"]

            specid = dataParam[0]["paramitems"][0]["valueitems"][0]["specid"]         #找出某个车的id
            list.append(specid)

            dataParam0 = dataParam[0]["paramitems"]  # 基本参数
            list0 = ['车型名称', '厂商指导价(元)', '厂商', '级别', '能源类型', '环保标准', '上市时间', '工信部纯电续航里程(km)',
                     '快充时间(小时)', '慢充时间(小时)', '快充电量百分比', '最大功率(kW)', '最大扭矩(N·m)', '发动机', '电动机(Ps)', '变速箱',
                     '长*宽*高(mm)', '车身结构', '最高车速(km/h)', '官方0-100km/h加速(s)', '实测0-100km/h加速(s)', '实测100-0km/h制动(m)',
                     '实测续航里程(km)', '实测快充时间(小时)', '实测慢充时间(小时)', '工信部综合油耗(L/100km)', '实测油耗(L/100km)', '整车质保']
            appendList0 = [nullDescriptor] * len(list0)
            dict0 = {}
            for i in range(len(list0)):
                dict0[list0[i]] = i
            for i in dataParam0:
                if i["name"] in dict0:
                    appendList0[dict0[i['name']]] = i['valueitems'][0]['value']
            for i in appendList0:
                list.append(i)

            dataParam1 = dataParam[1]["paramitems"]  # 车身
            list1 = ['长度(mm)', '宽度(mm)', '高度(mm)', '轴距(mm)', '前轮距(mm)', '后轮距(mm)', '最小离地间隙(mm)', '车身结构', '车门数(个)',
                     '座位数(个)', '油箱容积(L)', '行李厢容积(L)', '整备质量(kg)']
            appendList1 = [nullDescriptor] * len(list1)
            dict1 = {}
            for i in range(len(list1)):
                dict1[list1[i]] = i
            for i in dataParam1:
                if i["name"] in dict1:
                    appendList1[dict1[i['name']]] = i['valueitems'][0]['value']
            for i in appendList1:
                list.append(i)

            dataParam2 = dataParam[2]["paramitems"]  # 发动机
            list2 = ['发动机型号', '排量(mL)', '进气形式', '气缸排列形式',
                     '气缸数(个)', '每缸气门数(个)', '压缩比', '配气机构', '缸径(mm)', '行程(mm)', '最大马力(Ps)', '最大功率(kW)',
                     '最大功率转速(rpm)', '最大扭矩(N·m)', '最大扭矩转速(rpm)', '发动机特有技术', '燃料形式', '燃油标号', '供油方式', '缸盖材料',
                     '缸体材料', '环保标准']
            appendList2 = [nullDescriptor] * len(list2)
            dict2 = {}
            for i in range(len(list2)):
                dict2[list2[i]] = i
            for i in dataParam2:
                if i["name"] in dict2:
                    appendList2[dict2[i['name']]] = i['valueitems'][0]['value']
            for i in appendList2:
                list.append(i)

            dataParam3 = dataParam[3]["paramitems"]  # 电动机
            list3 = ['电机类型', '电动机总功率(kW)', '电动机总扭矩(N·m)', '前电动机最大功率(kW)', '前电动机最大扭矩(N·m)',
                     '后电动机最大功率(kW)', '后电动机最大扭矩(N·m)', '系统综合功率(kW)', '系统综合扭矩(N·m)', '驱动电机数', '电机布局',
                     '电池类型', '工信部纯电续航里程(km)', '电池能量(kWh)', '百公里耗电量(kWh/100km)', '电池组质保', '快充时间(小时)',
                     '慢充时间(小时)', '快充电量(%)']
            appendList3 = [nullDescriptor] * len(list3)
            dict3 = {}
            for i in range(len(list3)):
                dict3[list3[i]] = i
            for i in dataParam3:
                if i["name"] in dict3:
                    appendList3[dict3[i['name']]] = i['valueitems'][0]['value']
            for i in appendList3:
                list.append(i)

            dataParam4 = dataParam[4]["paramitems"]  # 变速箱
            list4 = ['挡位个数', '变速箱类型', '简称']
            appendList4 = [nullDescriptor] * len(list4)
            dict4 = {}
            for i in range(len(list4)):
                dict4[list4[i]] = i
            for i in dataParam4:
                if i["name"] in dict4:
                    appendList4[dict4[i['name']]] = i['valueitems'][0]['value']
            for i in appendList4:
                list.append(i)

            dataParam5 = dataParam[5]["paramitems"]  # 底盘转向
            list5 = ['驱动方式', '四驱形式', '中央差速器结构',
                     '前悬架类型', '后悬架类型', '助力类型', '车体结构', ]
            appendList5 = [nullDescriptor] * len(list5)
            dict5 = {}
            for i in range(len(list5)):
                dict5[list5[i]] = i
            for i in dataParam5:
                if i["name"] in dict5:
                    appendList5[dict5[i['name']]] = i['valueitems'][0]['value']
            for i in appendList5:
                list.append(i)

            list6 = ['前制动器类型', '后制动器类型', '驻车制动类型', '前轮胎规格', '后轮胎规格', '备胎规格']
            appendList6 = [nullDescriptor] * len(list6)
            if len(dataParam) == 7:
                dataParam6 = dataParam[6]["paramitems"]  # 车轮制动
                dict6 = {}
                for i in range(len(list6)):
                    dict6[list6[i]] = i
                for i in dataParam6:
                    if i["name"] in dict6:
                        appendList6[dict6[i['name']]] = i['valueitems'][0]['value']
            for i in appendList6:
                list.append(i)

            dataConfig = data["config"]

            dataConfig0 = dataConfig[0]["configitems"]  # 主/被动安全装备
            List0 = ['主/副驾驶座安全气囊', '前/后排侧气囊', '前/后排头部气囊(气帘)',
                     '膝部气囊', '副驾驶座垫式气囊', '后排安全带式气囊', '后排座椅防下滑气囊', '后排中央安全气囊', '被动行人保护', '胎压监测功能',
                     '缺气保用轮胎', '安全带未系提醒', 'ISOFIX儿童座椅接口', 'ABS防抱死', '制动力分配(EBD/CBC等)', '刹车辅助(EBA/BAS/BA等)',
                     '牵引力控制(ASR/TCS/TRC等)', '车身稳定控制(ESC/ESP/DSC等)', '并线辅助', '车道偏离预警系统', '车道保持辅助系统',
                     '道路交通标识识别', '主动刹车/主动安全系统', '夜视系统', '疲劳驾驶提示']
            AppendList0 = [nullDescriptor] * len(List0)
            Dict0 = {}
            for i in range(len(List0)):
                Dict0[List0[i]] = i
            for i in dataConfig0:
                if i["name"] in Dict0:
                    AppendList0[Dict0[i['name']]] = i['valueitems'][0]['value']
            for i in AppendList0:
                list.append(i)

            dataConfig1 = dataConfig[1]["configitems"]  # 辅助/操控配置
            List1 = ['前/后驻车雷达', '驾驶辅助影像', '倒车车侧预警系统',
                     '巡航系统', '驾驶模式切换', '自动泊车入位', '发动机启停技术', '自动驻车', '上坡辅助', '陡坡缓降', '可变悬架功能', '空气悬架',
                     '电磁感应悬架', '可变转向比', '中央差速器锁止功能', '整体主动转向系统', '限滑差速器/差速锁', '涉水感应系统']
            AppendList1 = [nullDescriptor] * len(List1)
            Dict1 = {}
            for i in range(len(List1)):
                Dict1[List1[i]] = i
            for i in dataConfig1:
                if i["name"] in Dict1:
                    AppendList1[Dict1[i['name']]] = i['valueitems'][0]['value']
            for i in AppendList1:
                list.append(i)

            dataConfig2 = dataConfig[2]["configitems"]  # 外部/防盗配置
            List2 = ['天窗类型',
                     '运动外观套件', '电动扰流板', '轮圈材质', '电动吸合车门', '侧滑门形式', '电动后备厢', '感应后备厢', '电动后备厢位置记忆',
                     '尾门玻璃独立开启', '车顶行李架', '发动机电子防盗', '车内中控锁', '钥匙类型', '无钥匙启动系统', '无钥匙进入功能',
                     '主动闭合式进气格栅', '远程启动功能', '车侧脚踏板', '电池预加热']
            AppendList2 = [nullDescriptor] * len(List2)
            Dict2 = {}
            for i in range(len(List2)):
                Dict2[List2[i]] = i
            for i in dataConfig2:
                if i["name"] in Dict2:
                    AppendList2[Dict2[i['name']]] = i['valueitems'][0]['value']
            for i in AppendList2:
                list.append(i)

            dataConfig3 = dataConfig[3]["configitems"]  # 内部配置
            List3 = ['方向盘材质', '方向盘位置调节', '多功能方向盘', '方向盘换挡',
                     '方向盘加热', '方向盘记忆', '行车电脑显示屏幕', '全液晶仪表盘', '液晶仪表尺寸', 'HUD抬头数字显示', '内置行车记录仪', '主动降噪',
                     '手机无线充电功能', '电动可调踏板']
            AppendList3 = [nullDescriptor] * len(List3)
            Dict3 = {}
            for i in range(len(List3)):
                Dict3[List3[i]] = i
            for i in dataConfig3:
                if i["name"] in Dict3:
                    AppendList3[Dict3[i['name']]] = i['valueitems'][0]['value']
            for i in AppendList3:
                list.append(i)

            dataConfig4 = dataConfig[4]["configitems"]  # 座椅配置
            List4 = ['座椅材质', '运动风格座椅', '主座椅调节方式', '副座椅调节方式', '主/副驾驶座电动调节',
                     '前排座椅功能', '电动座椅记忆功能', '副驾驶位后排可调节按钮', '第二排座椅调节', '后排座椅电动调节', '后排座椅功能', '后排小桌板',
                     '第二排独立座椅', '座椅布局', '后排座椅放倒形式', '后排座椅电动放倒', '前/后中央扶手', '后排杯架', '加热/制冷杯架']
            AppendList4 = [nullDescriptor] * len(List4)
            Dict4 = {}
            for i in range(len(List4)):
                Dict4[List4[i]] = i
            for i in dataConfig4:
                if i["name"] in Dict4:
                    AppendList4[Dict4[i['name']]] = i['valueitems'][0]['value']
            for i in AppendList4:
                list.append(i)

            dataConfig5 = dataConfig[5]["configitems"]  # 多媒体配置
            List5 = ['中控彩色液晶屏幕', '中控液晶屏尺寸', 'GPS导航系统', '导航路况信息显示', '道路救援呼叫', '中控液晶屏分屏显示', '蓝牙/车载电话',
                     '手机互联/映射', '语音识别控制系统', '手势控制', '面部识别', '车联网', 'OTA升级', '车载电视', '后排液晶屏幕', '后排控制多媒体',
                     '多媒体/充电接口', 'USB/Type-C接口数量', '车载CD/DVD', '220V/230V电源', '行李厢12V电源接口', '扬声器品牌名称', '扬声器数量']
            AppendList5 = [nullDescriptor] * len(List5)
            Dict5 = {}
            for i in range(len(List5)):
                Dict5[List5[i]] = i
            for i in dataConfig5:
                if i["name"] in Dict5:
                    AppendList5[Dict5[i['name']]] = i['valueitems'][0]['value']
            for i in AppendList5:
                list.append(i)

            dataConfig6 = dataConfig[6]["configitems"]  # 灯光配置
            List6 = ['近光灯光源', '远光灯光源', '灯光特色功能', 'LED日间行车灯', '自适应远近光', '自动头灯', '转向辅助灯', '转向头灯', '车前雾灯',
                     '前大灯雨雾模式', '大灯高度可调', '大灯清洗装置', '大灯延时关闭', '触摸式阅读灯', '车内环境氛围灯']
            AppendList6 = [nullDescriptor] * len(List6)
            Dict6 = {}
            for i in range(len(List6)):
                Dict6[List6[i]] = i
            for i in dataConfig6:
                if i["name"] in Dict6:
                    AppendList6[Dict6[i['name']]] = i['valueitems'][0]['value']
            for i in AppendList6:
                list.append(i)

            dataConfig7 = dataConfig[7]["configitems"]  # 玻璃/后视镜
            List7 = ['前/后电动车窗',
                     '车窗一键升降功能', '车窗防夹手功能', '多层隔音玻璃', '外后视镜功能', '内后视镜功能', '后风挡遮阳帘', '后排侧窗遮阳帘',
                     '后排侧隐私玻璃', '车内化妆镜', '后雨刷', '感应雨刷功能', '可加热喷水嘴']
            AppendList7 = [nullDescriptor] * len(List7)
            Dict7 = {}
            for i in range(len(List7)):
                Dict7[List7[i]] = i
            for i in dataConfig7:
                if i["name"] in Dict7:
                    AppendList7[Dict7[i['name']]] = i['valueitems'][0]['value']
            for i in AppendList7:
                list.append(i)

            dataConfig8 = dataConfig[8]["configitems"]  # 空调/冰箱
            List8 = ['空调温度控制方式', '后排独立空调', '后座出风口',
                     '温度分区控制', '车载空气净化器', '车内PM2.5过滤装置', '负离子发生器', '车内香氛装置', '车载冰箱']
            AppendList8 = [nullDescriptor] * len(List8)
            Dict8 = {}
            for i in range(len(List8)):
                Dict8[List8[i]] = i
            for i in dataConfig8:
                if i["name"] in Dict8:
                    AppendList8[Dict8[i['name']]] = i['valueitems'][0]['value']
            for i in AppendList8:
                list.append(i)

            lists.append(list)

        except Exception as e:
            pass
        finally:
            pass

print('-------------------------------------------------------------')
print("begin to write Files")
with open("data.csv", 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for i in lists:
        writer.writerow(i)
print("finished writing Files")
