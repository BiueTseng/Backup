#撰寫一個Python program : 要求使用者輸入兩個數字，然後印出這兩個數字的最大公因數
#一次輸入兩個以上的整數
# from BiueLib import gcd_test
# x,y = map(eval,input("請輸入兩個數字並用逗號 , 隔開 : ").split(',')) #.split()根據 ()內容去分割，預設為 ' '空格
# gcd_formula(x,y)
'''
#輸入多個字串到多個變數裡
a,b =input("請輸入兩個字串，並逗號隔開 : ").split(',')
print('a = %s ,b = %s'%(a,b))

#輸入多個數進入list
list_example = list(map(eval,input('請輸入一組數字，並逗號隔開 : ').split(',')))
print(list_example)
'''
'''
#輸入一組字串，且將字串分割成字元並一一存入list中
input_test = input('請輸入一組字串 : ')
x = [i for i in input_test]
# x = {i for i in input_test} # 也可用set，但結果為不重複且排序為set內定
print(x)
'''

#要求使用者樹入0~127中的一個數字，再印出對應的字元
try:
    letter = eval(input('請輸入0~127中的一個數字: '))
except:
    try:
        letter = eval(input('請重新輸入0~127中的一個數字: '))
    except:
        print('第二次錯誤，別鬧!!!')
else:
    result = chr(letter)
    print(f'輸入的數字為:{letter}，輸出的字元為:{result}' )

print([i for i in range(2,101,2)])
print(list(range(2,101,2)))
# for i in range(2,101,2):
#     print(i,end =', ')

##################################
##