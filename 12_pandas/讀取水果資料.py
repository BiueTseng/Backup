# 非常重要: 資料庫大忌-> 當資料庫欄位設定好，就不准再變更
# 資料庫設計一定要用 "日記帳"的方式做
import mysql.connector as mysql
conn=mysql.connect(host="mahaljsp.asuscomm.com",
                   user="lcc",
                   password="lcc0507",
                   database="cloud")
cursor=conn.cursor()
cmd="select * from fruit"
cursor.execute(cmd)
data=[]
for r in cursor.fetchall():
    data.append([str(r[1]),r[2],r[3],r[4],r[5]])
print(data)
cursor.close()
conn.close()



conn=mysql.connect(host="localhost",
                   user="BiueTseng",
                   password="BiuELighT-1202",
                   database="cloud")
cursor=conn.cursor()
cmd="insert into 水果銷售(日期, 國家, 水果, 數量, 單價) values (%s, %s, %s, %s, %s)"
cursor.executemany(cmd,data)
conn.commit()
cursor.close()
conn.close()