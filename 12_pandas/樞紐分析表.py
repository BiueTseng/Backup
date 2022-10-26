# 非常重要: 資料庫大忌-> 當資料庫欄位設定好，就不准再變更
# 資料庫設計一定要用 "日記帳"的方式做
import mysql.connector as mysql
import pandas as pd
dis=pd.options.display
dis.max_columns=None
dis.max_rows=None
dis.width=None
dis.max_colwidth=None

conn=mysql.connect(host="mahaljsp.asuscomm.com",
                   user="lcc",
                   password="lcc0507",
                   database="cloud")
cursor=conn.cursor()
cmd="select * from fruit"
cursor.execute(cmd)
idx = [d[0] for d in cursor.description]
idx.remove("id")
print(idx)
data=[]
for r in cursor.fetchall():
    data.append([str(r[1]),r[2],r[3],r[4],r[5]])

cursor.close()
conn.close()
#print(data)

df=pd.DataFrame(data , columns=idx)#.query("國家=='US'") #從資料庫這邊先拉單一國家
#print(df)

## pivot_table 為樞紐分析的函式，index是要用什麼分類
#table=df.pivot_table(index=['國家','水果','日期'])
table=df.pivot_table(index=['國家','日期'],columns=['水果'],values='數量',fill_value=0,aggfunc='sum')
table=table.query("國家=='US'") #
print(table)