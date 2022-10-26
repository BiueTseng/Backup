import numpy as np
np.random.seed(0)
a=np.random.randint(0,100,10)
print(a)

#第一種傳統方法
b=sorted(a) #傳回list格式
print(b)
#第二種方式
c=np.sort(a)#傳回陣列格式
print(c)
#演算法
