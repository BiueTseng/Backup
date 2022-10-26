#空姐錄取標準
#1. height >= 160
#2. age <= 45
#二者缺一不可
height = eval(input('請輸入身高: '))
age = eval(input('請輸入年紀: '))
if height >=160 and age<=45 :
    print('錄取')
else:
    print('不錄取，不符合資格')
'''
height age  status
180    30    V
180    50    X
150    30    X
150    50    X
-------------------------
and 真值表 :兩者都必須為True , 結果才會是 True



'''
