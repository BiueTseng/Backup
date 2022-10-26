import random
import numpy as np
#產生10個 0~1 之間的亂數，其格式亦為陣列
a = np.random.random(10)
print(a)
###############################
#底下使用python迴圈，效能及差
b=[random.random() for i in range(10)]
print(b)
#產生出10個介於 1~100之間的亂數(含1，但不含100)
c = np.randon.randint(1,100,10)
print(c)
#底下1~100之間(有包含100)
d =  [random.randint(1,5) for i in range(10)]
print(d)