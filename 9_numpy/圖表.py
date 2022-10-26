#pip install matplotlib
import numpy as np
#import matplotlb.pyplot as plt
import pylab as plt
#plt.legend()#圖例，翻譯:傳奇
# x = np.random.randint(1,100,10)
# y = np.random.randint(1,100,10)
# print(x);print(y)
# #Scatter 散佈圖
# plt.scatter(x,y ,c="g")
# plt.show()
####################################
rng = np.random.RandomState(1) #set seed
x=rng.randint(1,100,10)
y=rng.randint(1,100,10)
print(x);print(y)
plt.scatter(x,y,c="g",s=300)
plt.show()
