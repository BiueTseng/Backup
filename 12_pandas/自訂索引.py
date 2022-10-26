import pandas as pd
import numpy as np
idx=['mercury','venus','earth','mars','jupiter','saturn','uranus','netpune','pluto']
planets=['水星','金星','地球','火星','木星','土星','天王星','海王星','冥王星']

s=pd.Series(data=planets,index=idx)
print(s[8])
print(s['pluto'])

import mysql.connector as mysql

conn=mysql.connect(host="mahaljsp.asuscomm.com",
                   user="lcc",
                   password="lcc0507",
                   database="cloud")
cursor=conn.cursor()
cursor.execute("select * from 台灣股市")
ds = cursor.description
idx=[d[0] for d in ds]
print(idx)
# rs = cursor.fetchall() #取得全部資料
r=cursor.fetchone() #取得一筆資料，若使用迴圈大量存取fetchone()，雖較省記憶體，但會當機有bug
print(r)
#pd.Series也吃 tuple 資料格式
s=pd.Series(data=r,index=idx)
print(s[5]) #如果資料庫欄位太多，每次要找都要重算索引
print(s['收盤']) #用自訂索引就可以用關鍵字快速查詢