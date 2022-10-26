import mysql.connector as mysql
import pandas as pd
#設定程式碼呈現dataframe 結果筆數的參數
#完美列印:第一種
# pd.set_option('display.max_columns',None) # None指的是練印出的筆數:不設定
# pd.set_option('display.max_rows',None)# None指的是練印出的筆數:不設定
# pd.set_option('display.width',None)# None指的是練印出的寬度:不設定
# pd.set_option('display.max_colwidth',None)# None指的是練印出的欄寬:不設定
#完美列印:第二種
dis=pd.options.display
# print(dis.max_cols)
# print(dis.max_rows)
# print(dis.width)
# print(dis.max_colwidth)
dis.max_columns=None
dis.max_rows=None
dis.width=None
dis.max_colwidth=None





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




