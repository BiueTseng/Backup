#可以在一開始寫專案時這樣寫，紀錄log檔，再去細分錯誤種類
# import datetime
# while(True):
#     try:
#         pass
#     except Exception as e:
#         with open("log.txt","a") as f:
#             d=datetime.datetime.now()
#             f.write(f'{str(d)}:{e}')



#不論有沒有發生錯誤，finally都會被執行
#甚至下達 exit()，死之前都要執行finally
# try:
#     x=10
#     y=0
#     print(x/y)
#     exit()
# except Exception as e:
#     print(f'error:{e}')
#     exit()
# finally:
#     print("finally 區塊")

########################################
#應用
# try:
#     file =open('d:/test1.txt','r',encoding='utf-8')
#     print(locals().keys())
#     lines=file.read()
#     print(lines)
# except Exception as e:
#     #print("發生了不知名的錯誤")
#     print(f"發生錯誤:{e}")
# finally:
#     if 'file' in locals().keys():#判定檔案是否有開啟成功
#         file.close()
#     print("檔案已關閉")

#底下類似java 的try-catch-resource
try:
    with open("d:/test.txt",'r',encoding="utf-8") as file:
        lines=file.read()
        print(lines)
        #離開 with 區塊前，會自動幫我們closed()檔案
except FileNotFoundError as e: #沒有此檔案時
    print(e)
except IOError as e: #硬碟壞掉時
    print(e)
#此時finally就不需要了，因為自動幫我們close檔案