#旗標 : 使用不具任何意義的數字，代表某一件事: flag
#在月球插上美國國旗: 何意?? 月球是美國的
#數位化: 同樣使用某個數，代表某件事
'''
0: 單身
1: 已婚
2: 離婚
3: 同居
4: 同性戀
# '''
# sex =eval(input('請輸入性別(0~4): '))
# print("輸入錯誤")
# if sex==0:
#     status="單身"
#     print("允許聯誼")
# elif sex==1:
#     status="已婚"
#     print("拒收會員")
# elif sex==2:
#     status="離婚"
#     print("第二春聯誼會")
# elif sex==3:
#     status="同居"
#     print("別亂搞")
# else:
#     print("同性戀")
# #上列問題為輸入0~4以外的都是同性戀
# ####################################
# sex =eval(input('請輸入性別(0~4): '))
# if sex==0:
#     status="單身"
#     print("允許聯誼")
# elif sex==1:
#     status="已婚"
#     print("拒收會員")
# elif sex==2:
#     status="離婚"
#     print("第二春聯誼會")
# elif sex==3:
#     status="同居"
#     print("別亂搞")
# elif sex==4:
#     status="同性戀"
# else:
#     status="輸入錯誤"

# ####################################
try:
    sex =eval(input('請輸入性別(0~4): '))
    status = None
    #status = ""
    if sex<=4:
       print(f"輸入數字為:{sex}")
    else:
       print("請輸入性別0~4")
except :
   print('輸入錯誤，請重新輸入')
   try:
       sex = eval(input('請輸入性別(0~4): '))
       status = None
       if sex <= 4:
           print(f"輸入數字為:{sex}")
           if sex == 0:
               status = "單身"
               print("允許聯誼")
           elif sex == 1:
               status = "已婚"
               print("拒收會員")
           elif sex == 2:
               status = "離婚"
               print("第二春聯誼會")
           elif sex == 3:
               status = "同居"
               print("別亂搞")
           else:
               status = "同性戀"
               print("跑錯地方")
       else:
               status="輸入錯誤"
               print(status)
   except:
       print("第二次錯誤，你是故意的吧!!!")
else:
    if sex==0:
        status="單身"
        print("允許聯誼")
    elif sex==1:
        status="已婚"
        print("拒收會員")
    elif sex==2:
        status="離婚"
        print("第二春聯誼會")
    elif sex==3:
        status="同居"
        print("別亂搞")
    elif sex ==4:
        status ="同性戀"
        print("跑錯地方")
    else :
        status="輸入錯誤"
        print(status)

####################################
try:
    sex = eval(input('請輸入性別(0~4): '))
except:
    print('輸入錯誤，請輸入性別(0~4)')
    try:
        sex = eval(input('請輸入性別(0~4): '))
    except:
        print('第二次錯誤，你是故意的吧!!!')
else:
    status=""
    if sex==0:
        status="單身"
        print("允許聯誼")
    elif sex==1:
        status="已婚"
        print("拒收會員")
    elif sex==2:
        status="離婚"
        print("第二春聯誼會")
    elif sex==3:
        status="同居"
        print("別亂搞")
    elif sex ==4:
        status ="同性戀"
        print("跑錯地方")
    else :
        status="輸入錯誤"
        print(status)

