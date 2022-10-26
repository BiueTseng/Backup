import numpy as np
import pylab as plt

x = np.linspace(0,20,10)
print(x)
#a為斜率，b為截距
a = 0.5
b = 3
y = a*x + b
print(y)
plt.figure(figsize = (6,6))
plt.xlim(0,25)
plt.ylim(0,25)
plt.plot(x,y)
plt.scatter(x,y)
plt.show()


