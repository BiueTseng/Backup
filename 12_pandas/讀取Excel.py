import pandas as pd
df=pd.read_excel("台灣股市.xlsx",'員工資料表')
#df=pd.read_csv("台灣股市.xlsx")

print(df)

# C#意可寫入&讀取 Excel
# Microsoft.Office.Interop.Excel套件: 微軟開發的，效能極差，沒安裝Excel無法讀取
# NPOI: 第三方套件，效能極高，直接寫入Excel格式，不需要安裝Excel