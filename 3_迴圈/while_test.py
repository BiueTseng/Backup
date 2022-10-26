i=0
#無窮迴圈 :若沒改變i值，將會變成無窮迴圈
# while i<100:
#     print(i)
'''
當"="左右兩側都一樣時，可簡化如下
i = i + 5 : i+= 5
i = i - 5 : i-= 5
i = i * 5 : i*= 5
i = i / 5 : i/= 5
i = i % 5 : i%= 5

pikachu.level = 20
pikachu.level = pikachu.level +10
pikachu.level+=10


pass 只是一個關鍵字，當不想在函數內做任何事，加上一個pass就可執行
ex : while True:
          pass

'''
# #while 與 for差異
# while i<100:
#     print(i)
#     i=i+5
#
# for i in range(0,100,5):
#     print(i)
# ################
# while True:
#     a=input('請輸入一個數字:')
#     if a=='q':
#         break
#     print(a)
############################################
count,error_times ,= 0,0
while True:
    try:
        sex = eval(input('請輸入數字0~4: '))
        status =""
        if isinstance(sex,int):
            if sex==0:
                status="單身"
                suggest = "趕緊加入會員聯誼"
            elif sex==1:
                status="已婚"
                suggest = "請勿到處拈花惹草"
            elif sex==2:
                status="離婚"
                suggest = "尋找第二春聯誼會"
            elif sex==3:
                status="同居"
                suggest = "別亂搞對象"
            elif sex ==4:
                status ="同性戀"
                suggest = "跑錯地方"
            else :
                #status = ""
                #suggest = ""
                error_times +=1
        count += 1
        if  count == 1 and error_times == 0:
            print(f'輸入數字:{sex}，為{status}，建議{suggest}')
            break
        elif count == 1 and error_times ==1:
            print("輸入超出範圍，依照提示輸入")
        # elif:
        #
        else:
            print(f'未定意數字{sex}，你是新人類...')
            break



    except:
        print('輸入錯誤，請依照提示操作!!!')
        error_times+=1
        if error_times>=3:
            print("連續錯誤三次，已列黑名單")
            break
