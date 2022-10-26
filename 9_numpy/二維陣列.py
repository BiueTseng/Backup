import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape) #(2,3) 先印列 再印行
print(a.mean())
b =np.array([[  [1,2,3],[4,5,6],[7,8,9],[10,11,12]]  ,
             [[13,14,15],[16,17,18],[19,20,21],[22,23,24]]
             ])
print(b)
print(b.shape)
print(b.mean())
#四維: 並不是四度空間
#空間只有三度，沒有四度，別那麼沒水準
#四維: 比如加上時間，那麼四維就是指速度
#五維: 加上加速度這一個條件

c = np.zero([3,5]) #中括弧是為了多維度設計的
print(c)
d = np.ones([2,3,4])
print(d)