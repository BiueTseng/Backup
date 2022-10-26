'''
很重要，要記住
list       : a=[1,2,3,4,5]，a.append(10)
tuple      : b=(1,2,3,4,5) :不可變更
dictionary : c={"key":"value" ,"key":"value"}
set        : d=set([1,2,3,4,5])
'''
# import 輸入第三方套件
# Python 開發者 : 第一方 ，妳這個使用者:第二方，其他人開方的工具:第三方
# Anaconda :安裝時，python，ide一併安裝，並裝入大量第三方套件，肥大而慢
import random
import time
#第一種寫法 ，此法使用 Python的迴圈
a=[]
# time stamp 時間截記 1970/01/01~現在所經過的秒數
t1=time.time()
print(t1)
for i in range(1,100_001):
    a.append(i)
#print(a)
t2=time.time()
print(f'總花費{(t2-t1)*1000}ms')

##########
#第二種寫法 : 此法使用 C語言的迴圈
ta=time.time()
b = [i for i in range(1,100_001)]
#print(b)
tb=time.time()
print(f'總花費{(tb-ta)*1000}ms')
###########

c=[]
for i in range(100):
    c.append(random.randint(1,1000))
print(c)

d=[random.randint(1,1000) for i in range(100)] #建議熟悉此寫法
print(d)


#字典
#第一種寫法
m={"mercury":"水星","venus":"金星"}
#第二種寫法
n=dict(mercury="水星",venus="金星",earth="地球")
print(n)

#切片，子字串
s="abcdefghijklm"
#S[起始位置 : 結束位置(但不包含此位置) :步進值]
print(s[3:7]) #3~6
print(s[:]) #從頭抓到尾 ==print(s)
print(s[::2]) #從頭抓到尾，每隔2位抓一次

#跟附屬檔名有關
file="tiger.jpg"
print(file[:-4]) #-4從後面算來
print(s[::-1]) #反向選取 ==print(s[13::-1])

x=["mercury","venus","earth","mars"]
print(x[::-1])