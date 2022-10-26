import numpy as np
a=np.array([1,2,3,4,5])
b=np.zeros([10])+5 #習慣性加 "[]" 會跟二維以上有關係
# b[20]=5000 #指定某個元素
print(b)
c = np.ones([20])
print(c)
#使用c的迴圈一個一個改，速度極快
d=np.ones([20])*100
print(d)
##################
#list只能用迴圈一個一個改
#python的迴圈慢得要死
l = [1 for i in range(10)]
print(l)
for i in range(len(l)):
    l[i]=100
print(l)