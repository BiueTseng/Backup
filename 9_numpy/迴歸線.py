#regression
import numpy as np
import pylab as plt
n = 30
noise = 40*(np.random.random(n)*2-1)
print(noise)

x = np.linspace(22,40,n)
y = 500-x*10 + noise
# 0 <= noise < 1
# -1 <= 2*noise-1 < 1
plt.figure(figsize=(6,3))
plt.xlim(20,45)
plt.ylim(50,300)
plt.scatter(x,y)


args = np.polyfit(x,y,1)

print(args)
a=args[0] # 斜率
b=args[1] # 截距
# 第三個參數位置為:冪次方，即為要函數input的多項式最大次方
r = a*x + b
plt.plot(x,r,c='g')
plt.show()


##############################
# args = np.polyfit(x,y,6)
# f = np.poly1d(args) # 藉由參數，產生函數，可在高次方多項式時使用
## Line 30，31 可簡化下式
f = np.poly1d(np.polyfit(x,y,6))
plt.plot(x,f(x),c='g')
plt.show()




