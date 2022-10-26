#pip install xlrd openpyxl
#xlrd :讀取Eecel
#openpyxl
import mysql.connector as mysql
import pandas as pd

conn=mysql.connect(host="mahaljsp.asuscomm.com",
                   user="lcc",
                   password="lcc0507",
                   database="cloud")
cursor=conn.cursor()
cursor.execute("select * from 台灣股市")
ds = cursor.description
cols=[d[0] for d in ds]
#print(cols)
data=[]
for r in cursor.fetchall():
    data.append(r)
df=pd.DataFrame(data=data,columns=cols)
print(df)

#output excel檔
df.to_excel("台灣股市.xlsx",sheet_name = '員工資料表',index=False) #index=False DataFrame 的欄位索引不寫入

df.to_csv("台灣股市.csv",sheet_name = '員工資料表',index=False)