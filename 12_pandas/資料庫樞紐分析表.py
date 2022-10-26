import mysql.connector as mysql
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)
conn=mysql.connect(host='mahaljsp.asuscomm.com', user='lcc', password='lcc0507', database='cloud')
cursor=conn.cursor()
cmd="select 日期,"+\
"sum(case when 水果 = 'Apple' then 數量 else 0 end) as 蘋果,"+\
"sum(case when 水果 = 'Banana' then 數量 else 0 end) as 香蕉,"+\
"sum(case when 水果 = 'Orange' then 數量 else 0 end) as 柳橙,"+\
"sum(case when 水果 = 'Grape' then 數量 else 0 end) as 葡萄,"+\
"format(sum(單價*數量), 4) as 總價 "+\
"from fruit group by 日期 "+\
"order by 日期"


#資料量很大時，不要用 pd.pivot_table，要用SQL語法
cursor.execute(cmd)
cols=[d[0] for d in cursor.description]
#print(cols)
data=[]
for r in cursor.fetchall():
    data.append(r)
cursor.close()
conn.close()
df=pd.DataFrame(data ,columns=cols)
print(df)