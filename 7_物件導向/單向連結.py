#Single link 單向連結 :大二資料結構為必考題
# planets = ['mercury','venus']
# planets.append('earth')
#list :本身可以更改長度，一直到記憶體爆掉為止
#底下為函數: list 的結構
import random

class Node(): #節點
    def __init__(self):
        self.data = 0
        self.next = None
random.seed(0)#重下種子
datas=[random.randint(1,100) for i in range(10)]
# import numpy as np
# d1=np.random.randint(1,100,10)
print(datas)

root = Node()
index = root
# 步驟:
#
# index.data = datas[0]
# index.next = Node()
# index = index.next
#
# index.data = datas[1]
# index.next = Node()
# index = index.next
#
# index.data = datas[2]
# index.next = Node()
# index = index.next
#用迴圈
for d in datas:
    index.data = d
    index.next = Node()
    index = index.next
#遍訪
index = root #索引拉到最前面
while index.next is not None:
    print(index.data)
    index = index.next
#1. 別人做出來的，自己不一定寫得出來
#2. 站在巨人的肩膀上，死得更快