import numpy as np
import pylab as plt
x = [1,50]
y = [1,60]
plt.figure(figsize=(6,6))
plt.xlim([-100,100])
plt.ylim([-100,100])
plt.plot(x,y)
plt.savefig("test.jpg") #將圖表存成檔案
plt.show()