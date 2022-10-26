# import mysql.connector as mysql
# conn=mysql.connect(host="localhost",
#                    user="lcc",
#                    password="lcc0507",
#                    database="cloud")
# cursor=conn.cursor()
# cmd=f"insert into 台灣股市 (日期, 開盤, 最高, 最低) values ({'2022-09-29'}, 150, 160, 170, 140) "
# try:
#     cursor.execute(cmd)
#     conn.commit()
# except:
#     print("日期重複")
#
# conn.close()


#C/C++ 並沒有例外處理
#如果是要撰寫系統，或是韌體，或是駭客入侵程式，就必需使用C/C++
#應用程式，就必由 C#/Java/Kotlin/QT :發佈執行檔給客戶
#工具 : Python來撰寫
#java
# try{
#
# }
# catch(Exception e){
#
# }
import requests #由網路上下在圖片
from requests import HTTPError

try:
    #rint(10/0)

    #輸入網址
    page = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Walking_tiger_female.jpg/220px-Walking_tiger_female.jpg")
    with open('tiger.jpg','wb') as f:
        f.write(page.content)

except Exception as e: #錯誤也是一種物件
    # print(e)
    if str(e)=="division by zero":
        print("分母不可為0")
    else:
        print("不明錯誤")
print("程式要結束了喔...")