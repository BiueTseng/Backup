#tuple(元組)
a=(10,20,30,40)
print(a)
print(a[0])
for i in a:
    print(i)

#tuple 裡面的值，不可變更
#為了函數返回數值的，不被其他程式所更改
#a[0]=100 ->error
#a.append(100)->無此用法

#底下為純數字
b=(10)
print('b = ',b)
#底下為只有一個元素的tuple
c=(10,)
print('c=',c)
print('c[0]=',c[0])
#可變tuple，其實是變換list裡的東西
c=('abc','def',['thomas',80])
#c[0]="kkk" <-error
c[2][0]="tracy"
print(c)

#你別想用Python寫出一個很安全的程式
#Python是一個好用的工具