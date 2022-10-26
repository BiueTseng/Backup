#list : 列表

a=[10,20,30,40,50]
print(a)
print(a[0]) #在中括號內[0] 為索引值(index)
print(a[1])
#print(a[5]) #list out of range :超出索引範圍
print(len(a))#列出a的長度
print(type(a))#class list : 為list類別
#使用迴圈遍訪物件內所有元素
for i in range(len(a)): #i :0,1,2,3,4
    print(a[i])
print()
#使用for-each 遍訪物件內所有元素
for i in a: #i :10,20,30,40,50
    print(i)
'''
list :
1.像哆啦A夢的百寶袋，什麼都可以裝
2.list內的資料元素，可混和，可以不一樣
3.list內可以裝的容量，沒有數量限制，直到記憶體爆掉

'''
a = [1,2,3]
b = ['mercury',100,'venus',a,50]
for i in b:
    print(i)

#list 長度可以變更
c=['mercury','venus','earth']
print(c)
c.append('mars');c.append('jupiter')
print(c)

#產生1000個整數亂數，放在list裏
import random
n=10
Random_int = []  # 空 list
for i in range(n):
    Random_int.append(random.randint(1,200))
#print(Random_int)
sum=0
for i in Random_int :
     sum+=i
print(sum/n)

