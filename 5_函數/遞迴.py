#遞迴 :Recursive
#計算 5*4*3*2*1
# f(5)  =5*4*3*2*1
#       =5*f(4)
#       =5*4*f(3)
# .......
#        5*4*3*2*f(1)
#需要定義(1) =1
#Recursive : 自己呼叫自己，但不是真正的自己
def f(x):
    if x==1:
        return 1
    else:
        return x * f(x-1)
print(f(5))