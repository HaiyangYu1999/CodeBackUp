#!/usr/bin/env python3
import csv


class DailyWeather(object):
    def __init__(self, date):
        self.date=date
        self.DPreci = 0
        self.DaDewTemp = 0
        self.NDaDewTemp = 0
        self.DaDryTemp=0
        self.NDaDryTemp=0
        self.DaRelHum=0
        self.NDaRelHum=0
        self.DaSeaLPre=0
        self.NDaSeaLPre=0
        self.DaStationPre=0
        self.NDaStationPre=0
        self.DaVisibility=0
        self.NDaVisibility=0
        self.DaWetTemp=0
        self.NDaWetTemp=0
        self.DaWindDir=0
        self.NDaWindDir=0
        self.DaWindSpeed=0
        self.NDaWindSpeed=0
        self.ifCalculate=0
        self.Date=0
        self.DailyPrecipitation=0
        self.DailyDewPointTemp=0
        self.DailyDryTemp=0
        self.DailyRelativeHumidity=0
        self.DailySeaLevelPressure=0
        self.DailyStationPressure=0
        self.DailyVisibility=0
        self.DailyWetTemp=0
        self.DailyWindDirection=0
        self.DailyWindSpeed=0

    def addDpreci(self,Dpreci):
        if Dpreci=='':
            return
        if Dpreci=='T'or Dpreci=='' or Dpreci=='Ts':
            Dpreci=0
        else:
            if Dpreci[-1]=='s':
                Dpreci=Dpreci[:-1]
            Dpreci=float(Dpreci)
        self.DPreci+=Dpreci

    def addDaDewTemp(self,DaDewTemp):
        if DaDewTemp=='' or DaDewTemp=="*":
            return
        else:
            if DaDewTemp[-1]=='s':
                DaDewTemp=DaDewTemp[:-1]
            DaDewTemp=float(DaDewTemp)
            self.DaDewTemp+=DaDewTemp
            self.NDaDewTemp+=1

    def addDaDryTemp(self,DaDryTemp):
        if DaDryTemp=='' or DaDryTemp=="*":
            return
        else:
            if DaDryTemp[-1]=='s':
                DaDryTemp=DaDryTemp[:-1]
            DaDryTemp=float(DaDryTemp)
            self.DaDryTemp+=DaDryTemp
            self.NDaDryTemp+=1

    def addDaRelHum(self,DaRelHum):
        if DaRelHum=='' or DaRelHum=="*":
            return
        else:
            if DaRelHum[-1]=='s':
                DaRelHum=DaRelHum[:-1]
            DaRelHum=float(DaRelHum)
            self.DaRelHum+=DaRelHum
            self.NDaRelHum+=1

    def addDaSeaLPre(self,DaSeaLPre):
        if DaSeaLPre=='' or DaSeaLPre=="*":
            return
        else:
            if DaSeaLPre[-1]=='s':
                DaSeaLPre=DaSeaLPre[:-1]
            DaSeaLPre=float(DaSeaLPre)
            self.DaSeaLPre+=DaSeaLPre
            self.NDaSeaLPre+=1

    def addDaStationPre(self,DaStationPre):
        if DaStationPre=='' or DaStationPre=="*":
            return
        else:
            if DaStationPre[-1]=='s':
                DaStationPre=DaStationPre[:-1]
            DaStationPre=float(DaStationPre)
            self.DaStationPre+=DaStationPre
            self.NDaStationPre+=1

    def addDaVisibility(self,DaVisibility):
        if DaVisibility=='' or DaVisibility=="*":
            return
        else:
            if DaVisibility[-1]=='V' or DaVisibility[-1]=='s':
                DaVisibility=DaVisibility[:-1]
            DaVisibility=float(DaVisibility)
            self.DaVisibility+=DaVisibility
            self.NDaVisibility+=1

    def addDaWetTemp(self,DaWetTemp):
        if DaWetTemp=='' or DaWetTemp=="*":
            return
        else:
            if DaWetTemp[-1]=='s':
                DaWetTemp=DaWetTemp[:-1]
            DaWetTemp=float(DaWetTemp)
            self.DaWetTemp+=DaWetTemp
            self.NDaWetTemp+=1

    def addDaWindDir(self,DaWindDir):
        if DaWindDir=='' or DaWindDir=="VRB":
            return
        else:
            if DaWindDir[-1]=='s':
                DaWindDir=DaWindDir[:-1]
            DaWindDir=float(DaWindDir)
            self.DaWindDir+=DaWindDir
            self.NDaWindDir+=1

    def addDaWindSpeed(self,DaWindSpeed):
        if DaWindSpeed=='' or DaWindSpeed=="VRB":
            return
        else:
            if DaWindSpeed[-1]=='s':
                DaWindSpeed=DaWindSpeed[:-1]
            DaWindSpeed=float(DaWindSpeed)
            self.DaWindSpeed+=DaWindSpeed
            self.NDaWindSpeed+=1

    def calculate(self):
        self.Date=self.date
        self.DailyPrecipitation=self.DPreci

        self.DailyDewPointTemp="No data" if self.NDaDryTemp==0 else self.DaDewTemp/self.NDaDryTemp
        self.DailyDryTemp="No data"if self.NDaDryTemp==0 else self.DaDryTemp/self.NDaDryTemp
        self.DailyRelativeHumidity="No data"if self.NDaRelHum==0 else self.DaRelHum/self.NDaRelHum
        self.DailySeaLevelPressure="No data"if self.NDaSeaLPre==0 else self.DaSeaLPre/self.NDaSeaLPre
        self.DailyStationPressure="No data" if self.NDaStationPre==0 else self.DaStationPre/self.NDaStationPre
        self.DailyVisibility="No data"if self.NDaVisibility==0 else self.DaVisibility/self.NDaVisibility
        self.DailyWetTemp="No data"if self.NDaWetTemp==0 else self.DaWetTemp/self.NDaWetTemp
        self.DailyWindDirection="No data" if self.NDaWindDir==0 else self.DaWindDir/self.NDaWindDir
        self.DailyWindSpeed="No data" if self.NDaWindSpeed==0 else self.DaWindSpeed/self.NDaWindSpeed
        self.ifCalculate=1

    def print(self):
        if self.ifCalculate==0:
            raise ValueError("uncalculated data in "+self.date+"!")
        print('Date=',self.Date)
        print('DailyPrecipitation=',self.DPreci)
        print('DailyDewPointTemp=',self.DailyDewPointTemp)
        print('DailyDryTemp=',self.DailyDryTemp)
        print('DailyRelativeHumidity=',self.DailyRelativeHumidity)
        print('DailySeaLevelPressure=',self.DailySeaLevelPressure)
        print('DailyStationPressure=',self.DailyStationPressure)
        print('DailyVisibility=',self.DailyVisibility)
        print('DailyWetTemp=',self.DailyWetTemp)
        print('DailyWindDirection=',self.DailyWindDirection)
        print('DailyWindSpeed=',self.DailyWindSpeed)

    def add(self,wholedata):
        self.addDpreci(wholedata[3])
        self.addDaDewTemp(wholedata[5])
        self.addDaDryTemp(wholedata[6])
        self.addDaRelHum(wholedata[7])
        self.addDaSeaLPre(wholedata[8])
        self.addDaStationPre(wholedata[9])
        self.addDaVisibility(wholedata[10])
        self.addDaWetTemp(wholedata[11])
        self.addDaWindDir(wholedata[12])
        self.addDaWindSpeed(wholedata[13])


class MonthlyWeather(object):
    def __init__(self,month):
        self.month=month
        self.Day=[]
        self.data30=[0,]*10
        self.count30=[0,]*10
        self.data7=[0,]*10
        self.count7=[0,]*10

    def calculate7(self):
        day7=self.Day[-7:]
        for i in day7:
            if i.ifCalculate == 0:
                raise ValueError("uncalculated data in " + i.date + "!")
            if i.DailyPrecipitation!="No data":
                self.data7[0]+=i.DailyPrecipitation
                self.count7[0]=1
            if i.DailyDewPointTemp != "No data":
                self.data7[1] += i.DailyDewPointTemp
                self.count7[1] += 1
            if i.DailyDryTemp != "No data":
                self.data7[2] += i.DailyDryTemp
                self.count7[2] += 1
            if i.DailyRelativeHumidity != "No data":
                self.data7[3] += i.DailyRelativeHumidity
                self.count7[3] += 1
            if i.DailySeaLevelPressure != "No data":
                self.data7[4] += i.DailySeaLevelPressure
                self.count7[4] += 1
            if i.DailyStationPressure != "No data":
                self.data7[5] += i.DailyStationPressure
                self.count7[5] += 1
            if i.DailyVisibility != "No data":
                self.data7[6] += i.DailyVisibility
                self.count7[6] += 1
            if i.DailyWindDirection != "No data":
                self.data7[7] += i.DailyWindDirection
                self.count7[7] += 1
            if i.DailyWindSpeed != "No data":
                self.data7[8] += i.DailyWindSpeed
                self.count7[8] += 1
            if i.DailyWetTemp != "No data":
                self.data7[9] += i.DailyWetTemp
                self.count7[9] += 1
        for i in range(len(self.data7)):
            if self.count7[i]==0:
                self.data7[i]="No data"
            else:
                self.data7[i]/=self.count7[i]

    def calculate30(self):
        day30=self.Day[:]
        for i in day30:
            if i.ifCalculate == 0:
                raise ValueError("uncalculated data in " + i.date + "!")
            if i.DailyPrecipitation!="No data":
                self.data30[0]+=i.DailyPrecipitation
                self.count30[0]=1
            if i.DailyDewPointTemp != "No data":
                self.data30[1] += i.DailyDewPointTemp
                self.count30[1] += 1
            if i.DailyDryTemp != "No data":
                self.data30[2] += i.DailyDryTemp
                self.count30[2] += 1
            if i.DailyRelativeHumidity != "No data":
                self.data30[3] += i.DailyRelativeHumidity
                self.count30[3] += 1
            if i.DailySeaLevelPressure != "No data":
                self.data30[4] += i.DailySeaLevelPressure
                self.count30[4] += 1
            if i.DailyStationPressure != "No data":
                self.data30[5] += i.DailyStationPressure
                self.count30[5] += 1
            if i.DailyVisibility != "No data":
                self.data30[6] += i.DailyVisibility
                self.count30[6] += 1
            if i.DailyWindDirection != "No data":
                self.data30[7] += i.DailyWindDirection
                self.count30[7] += 1
            if i.DailyWindSpeed != "No data":
                self.data30[8] += i.DailyWindSpeed
                self.count30[8] += 1
            if i.DailyWetTemp != "No data":
                self.data30[9] += i.DailyWetTemp
                self.count30[9] += 1
        for i in range(len(self.data30)):
            if self.count30[i]==0:
                self.data30[i]="No data"
            else:
                self.data30[i]/=self.count30[i]

    def print(self):
        print("Month:=",self.month)
        print("Precipitation=",self.data30[0],self.data7[0])
        print("DewTemperature=",self.data30[1],self.data7[1])
        print("DryBulbTemperature=",self.data30[2],self.data7[2])
        print("RelativeHumidity=",self.data30[3],self.data7[3])
        print("SeaLevelPressure=",self.data30[4],self.data7[4])
        print("StationPressure=",self.data30[5],self.data7[4])
        print("Visibility=",self.data30[6],self.data7[6])
        print("WindDirection=",self.data30[7],self.data7[7])
        print("WindSpeed=",self.data30[8],self.data7[8])
        print("WetBulbTemperature=",self.data30[9],self.data7[9])


def getDailyWeather():
    data = []
    with open('WeatherData1996To1999.csv', 'r') as f:
        file = csv.reader(f)
        for item in file:
            data.append(item)
    with open('WeatherData2000To2009.csv', 'r') as f:
        file = csv.reader(f)
        for item in file:
            data.append(item)
    with open('WeatherData2010To2019.csv', 'r') as f:
        file = csv.reader(f)
        for item in file:
            data.append(item)
    dic = {}
    for i in data:
        if i[0] == 'DATE':
            continue
        date = i[0].split('T')[0]
        if date in dic.keys():
            continue
        dic.update({date: DailyWeather(date)})
    for i in data:
        if i[0] == 'DATE':
            continue
        date = i[0].split('T')[0]
        dic[date].add(i)
    for i in dic.keys():
        dic[i].calculate()
    return dic


def writeDailyWeather():
    dic=getDailyWeather()
    with open('DailyWeather.txt', 'w',newline='') as f:
        file = csv.writer(f)
        csv_in=[]
        csv_in.append('Date')
        csv_in.append('DailyPrecipitation')
        csv_in.append('DailyDewPointTemperature')
        csv_in.append('DailyDryBulbTemperature')
        csv_in.append('DailyRelativeHumidity')
        csv_in.append('DailySeaLevelPressure')
        csv_in.append('DailyStationPressure')
        csv_in.append('DailyVisibility')
        csv_in.append('DailyWetBulbTemperature')
        csv_in.append('DailyWindDirection')
        csv_in.append('DailyWindSpeed')
        file.writerow(csv_in)
        for i in dic.keys():
            csv_in = []
            csv_in.append(dic[i].Date)
            csv_in.append(dic[i].DailyPrecipitation)
            csv_in.append(dic[i].DailyDewPointTemp)
            csv_in.append(dic[i].DailyDryTemp)
            csv_in.append(dic[i].DailyRelativeHumidity)
            csv_in.append(dic[i].DailySeaLevelPressure)
            csv_in.append(dic[i].DailyStationPressure)
            csv_in.append(dic[i].DailyVisibility)
            csv_in.append(dic[i].DailyWetTemp)
            csv_in.append(dic[i].DailyWindDirection)
            csv_in.append(dic[i].DailyWindSpeed)
            file.writerow(csv_in)


def getAverage(monthlyDic):
    aver30=[0,]*10
    Naver30=[0,]*10
    aver7=[0,]*10
    Naver7=[0,]*10
    for i in monthlyDic.values():
        for j in range(10):
            if i.data7[j]!="No data":
                aver7[j]+=i.data7[j]
                Naver7[j]+=1
            if i.data30[j]!="No data":
                aver30[j]+=i.data30[j]
                Naver30[j]+=1
    for i in range(10):
        aver7[i]/=Naver7[i]
        aver30[i]/=Naver30[i]
    for i in monthlyDic.values():
        for j in range(10):
            if i.data7[j]=="No data":
                i.data7[j]=aver7[j]
            if i.data30[j]=="No data":
                i.data30[j]=aver30[j]


def getMonthlyWeather():
    dic=getDailyWeather()
    MonthlyDic = {}
    for i in dic.keys():
        splt=i.split("-")
        date = splt[0]+"-"+splt[1]
        if date in MonthlyDic.keys():
            continue
        MonthlyDic.update({date: MonthlyWeather(date)})
    for i in dic.values():
        idate=i.date.split("-")[0]+"-"+i.date.split("-")[1]
        MonthlyDic[idate].Day.append(i)
    for i in MonthlyDic.values():
        i.calculate7()
        i.calculate30()
    getAverage(MonthlyDic)
    return MonthlyDic

def writeMonthlyWeather():
    dic=getMonthlyWeather()
    with open('MonthlyWeather.txt', 'w',newline='') as f:
        file = csv.writer(f)
        csv_in=[]
        csv_in.append('Month')
        csv_in.append('MonthlyTotallyPrecipitation')
        csv_in.append('MonthlyAverageDewPointTemperature')
        csv_in.append('MonthlyAverageDryBulbTemperature')
        csv_in.append('MonthlyAverageRelativeHumidity')
        csv_in.append('MonthlyAverageSeaLevelPressure')
        csv_in.append('MonthlyAverageStationPressure')
        csv_in.append('MonthlyAverageVisibility')
        csv_in.append('MonthlyAverageWindDirection')
        csv_in.append('MonthlyAverageWindSpeed')
        csv_in.append('MonthlyAverageWetBulbTemperature')
        csv_in.append('MonthlyLast7DaysAveragePrecipitation')
        csv_in.append('MonthlyLast7DaysAverageDewPointTemperature')
        csv_in.append('MonthlyLast7DaysAverageDryBulbTemperature')
        csv_in.append('MonthlyLast7DaysAverageRelativeHumidity')
        csv_in.append('MonthlyLast7DaysAverageSeaLevelPressure')
        csv_in.append('MonthlyLast7DaysAverageStationPressure')
        csv_in.append('MonthlyLast7DaysAverageVisibility')
        csv_in.append('MonthlyLast7DaysAverageWindDirection')
        csv_in.append('MonthlyLast7DaysAverageWindSpeed')
        csv_in.append('MonthlyLast7DaysAverageWetBulbTemperature')
        file.writerow(csv_in)
        for i in dic.values():
            csv_in=[]
            csv_in.append(i.month)
            for e in i.data30:
                csv_in.append(e)
            for e in i.data7:
                csv_in.append(e)
            file.writerow(csv_in)


if __name__=="__main__":
    writeDailyWeather()
    writeMonthlyWeather()
