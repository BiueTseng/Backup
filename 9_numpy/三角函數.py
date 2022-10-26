import numpy as np
import pylab as plt
#等差級數
#(360-0)/(10-1) = 40
a = np.linspace(0,360,50)
print(a)
r = 100
x = r*np.cos(a*np.pi/180)
y = r*np.sin(a*np.pi/180)
print(x)
print(y)
plt.figure(figsize=(8,8)) #設定長寬比例
plt.xlim([-120,120]) #X軸的尺度設定
plt.ylim([-120,120]) #Y軸的尺度設定
plt.scatter(x,y ,c='r') #畫點
plt.plot(x,y ,c = 'g') #畫線
plt.show()






