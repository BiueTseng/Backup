import pandas as pd
#from datetime import datetime
#from datetime.py import datetime類別
import datetime
import time
#import datetime.py檔
dates=pd.date_range('2022/2/20',periods=20) #periods產生20天的日期
print(dates)

#取得目前系統時間 :以TimeStamp秒數為單位，後面有小數，代表 ms
#TimeStamp :時間截記:自1970/01/01 00:00:00到現在所經歷過的秒數
t1=time.time()
print(f'{t1:,}秒')

#手動驗證
a=(2022-1970)*365*86400+(9*30*86400)
print(f'{a:,}秒')

#目前時間，格式為datetime
d1=datetime.datetime.now()
#指定日期
d2=datetime.datetime(1970,1,1)
diff=d1-d2
print(f'差了{diff.days:,}天') #兩個日期間差幾天
print(f'差了{diff.days*86400:,}秒')#兩個日期間差幾秒

#轉成字串: str from time
s1=d1.strftime('%Y-%m-%d')#(Y:年，m:月，d:日)
print(s1)
s2=d1.strftime('%H-%M-%S')#(H:時，M:分，S:秒)
print(s2)

#範例
d3=datetime.datetime(2022,1,1)
d4=datetime.datetime(2022,10,2)
d=d1-d3
print((d.days+6)%7) #算今天星期幾 (+6的意思是 計數從0開始記)
print(d1.strftime('%Y-%m-%d :%w')) #顯示今天星期幾
print(d1.strftime('%w=W')) #顯示今天是今年的第幾週

#2022/01/01是第二條路線，四天一輪，那今天要跑哪一條路線
d=d1-d2
print(f'今天要跑:{(d.days+2)%4}路線')

#往前幾天，往後幾天
d1=datetime.datetime.now()
d2=d1+datetime.timedelta(days=10)
#datetime.py的 timedelta類別
print(d2)

d5=d1+datetime.timedelta(days=-2)
print(d5)
############################################################

############################################################
#也可以用這一招避開，package名稱跟裡面類別名稱一樣的狀況
from datetime import timedelta
from datetime import datetime
#目前時間，格式為datetime
d1=datetime.now()
#指定日期
d2=datetime(1970,1,1)
diff=d1-d2
print(f'差了{diff.days:,}天') #兩個日期間差幾天
print(f'差了{diff.days*86400:,}秒')#兩個日期間差幾秒

#轉成字串: str from time
s1=d1.strftime('%Y-%m-%d')#(Y:年，m:月，d:日)
print(s1)
s2=d1.strftime('%H-%M-%S')#(H:時，M:分，S:秒)
print(s2)

#範例
d3=datetime(2022,1,1)
d4=datetime(2022,10,2)
d=d1-d3
print((d.days+6)%7) #算今天星期幾 (+6的意思是 計數從0開始記)
print(d1.strftime('%Y-%m-%d :%w')) #顯示今天星期幾
print(d1.strftime('%w=W')) #顯示今天是今年的第幾週

#2022/01/01是第二條路線，四天一輪，那今天要跑哪一條路線
d=d1-d2
print(f'今天要跑:{(d.days+2)%4}路線')

#往前幾天，往後幾天
d1=datetime.now()
d2=d1+timedelta(days=10)
#datetime.py的 timedelta類別
print(d2)

d5=d1+timedelta(days=-2)
print(d5)

import numpy as np
d1=datetime.now().strftime("%Y-%m-%d")
days=pd.date_range(d1, periods=10)
df=pd.DataFrame(np.random.randn(10,4),index=days,columns=['香蕉','蘋果','芒果','柳丁'])
print(df)

