#print(1)
#print(2)
#print(3)
#惰性函數: range(起始值，結束值)但"結束值"不包含結束值
for i in range(1,101):
    print(i)
##########
sum = 0
for i in range(1,101):
    sum=sum+i
    print(sum)
#通常外迴圈用i，內迴圈用 j
##test example##
#使用最快的方法計算1+2+3...+100
print((1+100)*100/2)
