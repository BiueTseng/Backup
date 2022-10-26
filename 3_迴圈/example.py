
'''
第一題: 試印出 : 1 2 3 4 5 6 7 8 9 10
'''
print("第一題")
for i in range(1,11):
    print(f'{i} ',end='') #建議寫法，這樣比較容易除錯
    #print(i,end=' ') #此寫法也可
print() #加入空白行 使得下一次結果不繼續接著

'''
第二題:試印出
*
*
*
*
*
'''
print("第二題")
for i in range(5): #i只是一個計數器
    print("*")
'''
第三題:試印出
* * * * *
'''
print("第三題")
for i in range(5):
    print('* ',end='')
print()
'''
第四題:試印出
* * * * *
* * * * *
* * * * *
'''
print("第四題")
#法一
for i in range(3):
    print('* * * * *',end='\n')
print()
#法二 (巢狀迴圈 Nested)
for i in range(3):
    for j in range(5):
        print(f'* ',end='')
    print()
'''
第五題:試印出 9X9 乘法表
 1 2 3 4 5 6 7 8 9 
 2 4 6   10
 3 6 9  ... ... 27
 . . .           .
 . .    .        .
 . .      .      .
 9 18 27 ... ... 81
'''
print("第五題")
for i in range(1,10):
    for j in range(1,10):
        print(f'{i*j:2d} ',end='')
        #2d:列印出兩個數字，不足兩個數，前面用空格，也就是靠右對齊
    print()
print()
result1 ,result2 ='',''
for i in range(1,10):
    result1=''
    for j in range(1,10):
        result1 += str(i) +'*'+str(j)+'='+str(i*j)+'\t'
    result2 += result1 + '\n'
print(result2)
'''
第六題:試印出
*
* *
* * * 
* * * *
* * * * *
'''
print("第六題")
#法一
for i in range(6):
    for j in range(i):
        print('* ',end='')
    for j in range(5-i):
        print(' ',end='')
    print()
#法二
for i in range(6):
    print('* '*i)
print()

#老師方法
for i in range(5):
    for j in range(i+1):
        print('* ',end='')
    print()
print()
'''
第七題:試印出
           列  *  空格
* * * * *  0   5   0
* * * *    1   4   1
* * *      2   3   2
* *        3   2   3
*          4   1   4
'''
print("第七題")
#法一
for i in range(5):
    for j in range(5-i):
        print('* ',end='')
    print()
print()
#法二
for i in range(5,0,-1):
    for j in range(i):
        print('* ',end='')
    print()


'''
第八題:試印出
           | 列  空格  *
        *  | 0   4    1
      * *  | 1   3    2
    * * *  | 2   2    3
  * * * *  | 3   1    4
* * * * *  | 4   0    5
'''
print("第八題")
for i in range(6):
    print('  '*(5-i) +'* '*i,end='')
    print()
print()
for i in range(5):
    for j in range(4-i):
        print('  ',end='')
    for j in range(i+1):
        print('* ',end='')
    print()

'''
第九題:試印出
> > > > >
< < < < <
> > > > >
< < < < <
> > > > >
'''
print("第九題")
for i in range(5):
    for j in range(5):
        if i%2==0:
            print('> ',end='')
        else:
            print('< ',end='')
    print()
'''
第十題:試印出
a a a a a
b b b b b
c c c c c
a a a a a
b b b b b
'''
print("第十題")
for i in range(5):
    for j in range(5):
        if i%3==0:
            print('a ',end='')
        elif i%3==1:
            print('b ',end='')
        else:
            print('c ',end='')
    print()

##############
print("######################")
n = eval(input('請輸入金字塔高度(1~30):'))
for i in range(1,n+1):
    print(' '*(n-i),'*'*(2*i-1))