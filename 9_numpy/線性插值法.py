#pip install scipy , scipy 是科學函數的套件--science
import numpy as np
import pylab as plt
from scipy.interpolate import interp1d

t= np.linspace(0,10,10)
noise=(np.random.random(10)*2-1)*0.1 #產生介於-0.1~0.1 之間的亂數
print(noise)
y=np.sin(2*np.pi*t)+noise
print(noise)
# plt.scatter(t,y) #畫點散圖
# plt.plot(t,y) #畫直線
plt.plot(t,y, 'go') #有第三個參數時，可以調整圖形繪製的類型，r為顏色，o圓形，s矩形，^三角形
# plt.show()


x=np.linspace(0,10,50)
#底下為二元一次方程式
#f=interp1d(t,y)#利用interp1d函數，再依t,y內產生插值的函數

#底下為一元三次方程式
f=interp1d(t,y , kind = 'cubic') #cubic為立方，即產生三次多項式

plt.plot(x,f(x),'ro')
plt.plot(x,f(x),c='yellow')
plt.show()
print(noise)
