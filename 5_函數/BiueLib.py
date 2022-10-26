#BiueLib函數庫

import math
def c2f(c):
    f=c*9/5+32
    print(f)
    #return None

def f2c(f):
    c=(f-32)*5/9
    return c #返回值 : return

# print(c2f(100))  #==> output: None
# x=f2c(212)
# print(x)

#改名稱，為了日後方便維護
#一個專案如果寫10天，有可能2天是在改名子

def point(r, angle):
    x= r*math.cos(angle * math.pi/180) #算半徑 r 的圓每度多少弧長
    y= r*math.sin(angle * math.pi/180)
    return x, y #多值返回

def circle(r, angle):
    x= r*math.cos(angle * math.pi/180) #算半徑 r 的圓每度多少弧長
    y= r*math.sin(angle * math.pi/180)
    # 多值返回，其實只返回一個值
    return x, y #多值返回
#     #return (x,y) tuple格式

def gcd_formula(x,y):
    #import math
    a = math.gcd(x ,y )
    print(f'輸入數字為 : ({x},{y}), 兩數字的最大公因數為 : {a}')
    return a
def gcd_manual(x,y):
    for factor in range(x,0,-1):
        if x % factor ==0 and y % factor ==0:
            return factor
######################################################################
#程式進入點，由此開始 : 呼叫函數
#當程式碼太長時，方便維護使用
'''
if  __name__=='__main__':
    add(110,10)
'''
'''
#以下為if __name__=='__main__'說例
#A版本 :無if __name__=='__main__'
def A_fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return  1
    else:
        #return 呼叫函數本身為"遞迴" 概念
        return A_fibonacci(n-2)+A_fibonacci(n-1)
for i in range(3):
    print(A_fibonacci(i))
####################################
#B版本 :有if __name__=='__main__'
def B_fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return  1
    else:
        #return 呼叫函數本身為"遞迴" 概念
        return B_fibonacci(n-2)+B_fibonacci(n-1)
if __name__=='__main__':
    for i in range(3):
        print(B_fibonacci(i))

#執行結果可在"調用函數庫內查閱"
#B版本中的if __name__=='__main__'這段程式碼作用為:
# 當 B_fibonacci函數在其他.py檔中被引用時，會先執行if __name__=='__main__'
# 若"False"則底下的程式碼就不會再被執行一次
'''
