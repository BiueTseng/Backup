#pip install plotly-express
#plotly-express是一種精美繪製圖表套件，比matplotlib還要強
import plotly_express as px
import pandas as pd
dis=pd.options.display
dis.max_columns=None
dis.max_rows=None
dis.width=None
dis.max_colwidth=None


df=px.data.gapminder()
#country:國家, continent:州別, gdpPercap:國民所得, iso_alpha:國別代碼,
#lifeExp :平均壽命, pop:人口數

#DataFrame可以使用類似資料庫的查詢功能
#df=df.query("country=='Taiwan'")
df=df.query("year==2007")
#print(df)

#讀取列
# ls=df.values
# for i in range(10,20):
#     print(ls[i])

#df.values[[0,1,2,3,4]] 外面是索引，裡面的[]是list，這是df的功能
#同理df.values[[:5]]
ls=[df.values[[x for x in range(10,20)]]]
print(ls)
#print(df.valuesd.dtype)
#df.values是object，不是物件


#idx=['mercury','venus','earth','mars','jupiter','saturn','uranus','netpune','pluto']
#idx[[3:6]] ，是錯誤的list裡只能是整數，或是切片[:5]

#讀取儲存格[列,行]
print(df.iloc[0,0]) #第0列第0行
print("=========單列時===========")
print(df.iloc[0,]) #第0列的所有行，傳回DataFrame格式
#也可print(df.iloc[0, :]) #第0列的所有行，傳回DataFrame格式
print("=========切片時===========")
print(df.iloc[0:2,])#列切片時，就會橫向列印，，傳回DataFrame格式

#讀取整行資料
#外面的[]是索引，裡面的[]是list，，傳回DataFrame格式
df_3=df[['country','continent','year']]
print(df_3)

#每個欄位的名稱，又稱為特徵，是AI機器學習的重要觀念
