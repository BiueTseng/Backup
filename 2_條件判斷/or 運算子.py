#疫苗優先施打
#kind : 第一類
#age >=65
kind = eval(input('請輸入第幾類: '))
age = eval(input('請輸入年紀: '))
if kind ==1 or age>=65:
    print('優先施打')
else:
    print('放生')
'''
左右二邊要有一個成立，結果就會成立
kind age result
1    70    V
1    25    V
9    70    V
9    25    X
--------------------------


'''