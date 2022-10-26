# 使用 Python 連線 Mysql時，需要驅動程式
# mysqlclient : 官方版本(oracle)，由c/c++寫成，效能高
# mysql-connector-python :官方版本，純Python寫成，執行ORM時效能高過mysqlclient
# pymysql :日本人寫的，純Python寫成，效能極差
import mysql.connector as mysql
import pylab as plt
import numpy as np
#建立連線
conn = mysql.connect(host = "mahaljsp.asuscomm.com",
                     user = "lcc",
                     password = "lcc0507",
                     database = "cloud")
#建立執行命令的物件 - cursor : 游標
cursor = conn.cursor()
#Python 內用輸入指令SQL的字串，請使用雙印號""
#而SQL語法請使用單引號''
cmd = "select * from 台灣股市 where 日期>='2022-01-01' order by 日期"
cursor.execute(cmd)
rs =cursor.fetchall() #recordSet
#print(range(len(rs)))
# for r in rs:
#     print(r)
x = list(range(len(rs)))
y = [r[5] for r in rs]
plt.figure(figsize=(12,6))
plt.scatter(x,y, c ='b')
#回歸線
f = np.poly1d(np.polyfit(x,y,10))
plt.plot(x,f(x),c='r')
plt.show()
#print(x)