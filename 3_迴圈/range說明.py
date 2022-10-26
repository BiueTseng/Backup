###只印 "range(1,11)"
print(range(1,11))
###list 會強迫惰性函數執行 next()，直到最後
print(list(range(1,11)))
print(list(range(11)))#起始值為0時，可省略
print(list(range(1,10,2)))#range(起始值，結束值，步進值)
print(list(range(10,1,-2)))#步進值為負值時，起始值要比結束值大
print("第一列","第二行","第三行","第四行")#使用","都會出現空白
#若不想空白，就要用格式化列印
print("%s%s%s"% ("第一行","第二行","第三行"))
print("第二列", end='') #沒有結數字元，預設是'\n'(換行)
print('第三列')
