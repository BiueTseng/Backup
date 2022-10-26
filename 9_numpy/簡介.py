#numpy(爛派) 是一套統計學的套件(科學計算套件)
#其中的格式 :就是矩陣 :矩陣的長度，一但定下，就不能變更
#pip install numpy
import numpy as np
l = [1,2,3,4,5]
a = np.array(l)
print(l[0])
print(a[0])
#遍訪方法
for i in range(len(a)):
    print(a[i])

for x in a : print(x)
##########
# l.append(20) list可以append()
# a.append(20) <==error，陣列一但決定便無法更改長度
# 因為陣列無法改長度，所以效能上，比 list高出好幾千倍
# 系統上，並沒有陣列，只有list。 所以MTA不考陣列
# 陣列必須依靠第三方套件 numpy