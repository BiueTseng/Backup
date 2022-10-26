#24節氣，是地球繞太陽的公轉軌道
#每19年，國曆與農曆會同一天
#一甲子為60年，為什麼不是 sky & land 的120種組合，因為沒有 甲丑, 乙子等倒序組合

from datetime import datetime
sky = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
land = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
animal = ['鼠','牛','虎','兔','龍','蛇','馬','羊','猴','雞','狗','豬']
# print(datetime.now().year)
# print(datetime.now().month)
# print(datetime.now().day)
# print(datetime.now().hour)
# print(datetime.now().minute)
# print(datetime.now().second)
yyy=datetime.now().year-1911
#print(yyy)
first = 13 #民國13年為甲子年
for i in range(150):
    year=first+i
    if year <= yyy:
        print(f'民國{year:3d}年 : {sky[i%10]}{land[i%12]} : {animal[i%12]} :{yyy-year+1}歲')
        #3d 為印出三個單位，不足三位補空格->即向右對齊
    else:
        print(f'民國{year:3d}年 : {sky[i % 10]}{land[i % 12]} : {animal[i % 12]}')