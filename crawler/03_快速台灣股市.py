#https://www.twse.com.tw/indicesReport/MI_5MINS_HIST?response=json&date=20221101
#更改後面 date的日期即可
import json
import random
import time

import mysql.connector as mysql
import requests
# 底下為教學範例
# month = 6
# # month:02d => 0(如果只有1位數，則此部分補 0) 2(兩位數) d (為整數)
# # 後面的日期修改無用
# url = f"https://www.twse.com.tw/indicesReport/MI_5MINS_HIST?response=json&date=2022{month:02d}01"
# print(url)
# page = requests.get(url)
# print(page.text)
# stock = json.loads(page.text)
# print(stock["data"])
# #print(stock["fields])
###############################################################################
#底下為完整快速台灣股市爬蟲
def getStock(year,month):
    url = f"https://www.twse.com.tw/indicesReport/MI_5MINS_HIST?response=json&date={year}{month:02d}01"
    page = requests.get(url)
    rows = json.loads(page.text)["data"]
    ls = []
    for row in rows:
        # print(row)

        ds =row[0].split("/")
        ls += [[f'{int(ds[0])+1911}/{ds[1]}/{ds[2]}',
               float(row[1].replace(",","")),
               float(row[2].replace(",","")),
               float(row[3].replace(",","")),
               float(row[4].replace(",",""))
               ]]
    return ls
datas=[]
year = 2022
month = 12
conn = mysql.connect(host ="localhost",
                         user = "BiueTseng",
                         password = "BiuELighT-1202",
                         database = "cloud")
cursor = conn.cursor()
cmd = "insert into 台灣股市 (日期, 開盤, 最高, 最低, 收盤) values (%s, %s, %s, %s, %s)"
for m in range(1,month):
    datas = []
    print(f"處理{year}/{m:02d}月資料")
    datas += getStock(year,m)
    cursor.execute(f"delete from 台灣股市 where 日期 like '{year}-{m:02d}%'")
    conn.commit()

    cursor.executemany(cmd, datas)
    conn.commit()
    #一定要sleep，否則會被鎖ip
    time.sleep(random.randint(5,8)+random.random())
print(datas)



cursor.close()
conn.close()