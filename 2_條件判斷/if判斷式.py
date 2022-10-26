'''
基本語法
if 條件:
    pass
else:
    pass
程式定義: 有人寫了二三十年，不知何謂程式
1. 一行一行往下執行
2. 具有 if判斷式
    當條件成立: 執行或不執行
    就是為了要跳行
3. 具需具有迴圈的功能: 就是為了省時
html/css: 並不是程式，只是區塊標籤
JavaScript也是一種程式語言
'''
'''
print("便當")
print("雞腿")
if 有獎金 :
    print("龍蝦")
else
    print("香蕉")
print(6)
print(7)
...
print(100)
'''
# 防呆法可參考
# try:
#     salary = int(input('請輸入薪水:'))
# except:
#     print('輸入錯誤')

#if 判斷式範例一
#Ctrl + "/"將所選區域全部註解
salary = eval(input('請輸入薪水:'))
if salary <= 30000:
    print("香蕉")
    print("請再加點油，努力點!!!")
else:
    if salary <= 60000:
        print("鮑魚")
    else:
        if salary <= 90000:
            print("龍蝦")
        else :
            print("滿漢全席")

#if 判斷式範例二
#底下是四選一
salary = eval(input('請輸入薪水:'))
if salary <= 30000:
    print("香蕉")
elif salary <= 60000:
    print("鮑魚")
elif salary <= 60000:
    print("龍蝦")
else:
     print("滿漢全席")

'''
範例一範例二運算效能上沒有差別
只是範例二較接近人類的思考，且撰寫容易辨認
'''
status = None
status1 = ""
dir(status)
type(status1)
