#使用時機: 進行資料大量搬移時

import mysql.connector as mysql
conn = mysql.connect(host = "mahaljsp.asuscomm.com",
                     user = "lcc",
                     password = "lcc0507",
                     database = "cloud")
cursor = conn.cursor()
cmd = "select * from 台灣股市 order by 日期"
cursor.execute(cmd)
rs =cursor.fetchall()
# for r in rs:
#     print(r)
cursor.close()
conn.close()
#跟本機的資料庫連線
conn = mysql.connect(host = "localhost" ,user ="BiueTseng",password="BiuELighT-1202",database="cloud")
cursor = conn.cursor()

data=[]
for r in rs:
    data.append([str(r[1]), r[2], r[3], r[4], r[5]])
#data 格式[['2000-01-01',100,150,140,100],[...],[,,,]]
print(data)
cmd="insert into 台灣股市 (日期, 開盤, 最高, 最低, 收盤) values (%s, %s, %s, %s, %s )"
cursor.executemany(cmd, data)#只開一次連線，然後將所有資料一次性寫入
conn.commit()
cursor.close()
conn.close()