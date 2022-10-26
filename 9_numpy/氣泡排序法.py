#禁止使用 python 執行此法 - 效能非常低
#1. 大學二年級資料結構必考題
#2. np.sort()就是使用類似方法，再使用 C 語言執行
#3. 很多人都說--> 別人已經做出來了，但不是自己做出來了。
#規則 : 假設有 n 個數(0 ~ n-1)
#      第i(0 ~ n-2)個數，要跟後面相比(i+1 ~ n-1)，如果前面的值較大，則對調
import time
import numpy as np
np.random.seed(0)
n=10000
a=np.random.randint(0,100,n)
# print(a)
# a=np.sort(a)
#print(a)
t1 =time.time()
for i in range(0,n-2+1): # +1 是因為range()函數的尾端並不包含
    for j in range(i+1,n-1+1):
        if a[i]>a[j]:
            # tmp=a[i]
            # a[i]=a[j]
            # a[j]=tmp
            a[i],a[j]=a[j],a[i] #快速方法
    #print(f'i={i}, {a}')
t2=time.time()
#print(a)
print(f'總花費{t2-t1}秒')