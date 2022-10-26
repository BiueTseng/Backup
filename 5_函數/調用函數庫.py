# from 調用函數 import 需球函數
# 也可 from 調用函數 import * =>加'*'為全部呼叫
# from BiueLib import c2f
# from BiueLib import f2c
# f=c2f(100)
# print(f)
# print(f2c(212))

print("----------A_fibonacci-----------")
from BiueLib import A_fibonacci
from BiueLib import B_fibonacci
A_example= A_fibonacci(5)
print(A_example)
print("-----------B_fibonacci----------")
B_example= B_fibonacci(5)
print(B_example)

from BiueLib import circle
r=100
for a in range(0,360):
    print(circle(r,a))

# 法一 :Terminal -->  pip install matplotlib
# 法二 : 左上角"File"->"settings"-> 專案(Project): 20220726_start class-> Python interpreter
#        ->package 輸入要install的package 名稱
#matplotlib為繪製圖表的套件
import pylab as plt # as 別名
r=100
#第一種寫法
# x=[]
# y=[]
# for a in range(0,361,20):
#     x1 ,y1=circle(r,a)
#     x.append(x1)
#     y.append(y1)
#     print(x1,y1)
#
#第二種寫法
for a in range (0,361,20):
    print(circle(r,a))
x=[circle(r,a)[0] for a in range(0,361,20)]  #[]為索引函數
y=[circle(r,a)[1] for a in range(0,361,20)]


plt.figure(figsize=(6,6)) #設定圖形長寬比
plt.xlim(-100,100) #限定x軸範圍
plt.ylim(-100,100) #限定y軸範圍

plt.plot([-100,100],[0,0])
plt.plot([0,0],[-100,100])
plt.plot(x,y)
#有'ro' :畫點, 沒ro是畫線
plt.plot(x,y, 'ro')
plt.show()
