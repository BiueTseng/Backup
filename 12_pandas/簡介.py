#pip install pandas
#pandas 是模擬 Excel的資料格式
#pandas 有兩種資料格式，1 是 Series， 2是 DataFrame
import pandas as pd
import numpy as np
#傳入 Series 的格式，可以是list

s1 = pd.Series([10,20,30,40,50])
#前面一行為索引，後面一行才是值
print(s1)
for s in s1:
    print(s)
print()
for i in range(len(s1)):
    print(s1[i])
#傳入 Series 的格式，可以是numpy的陣列，效能會比list高很多
'''
ls=[1,2,3,4,5]
ls.append(10)

a=np.array([1,2,3,4,5])
'''
s2=pd.Series(np.array([11,12,13,14,15]))
print(s2)

s3=pd.Series([11,12,13,14,15])

import cv2
img=cv2.imdecode