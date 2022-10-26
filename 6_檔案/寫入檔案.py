#a :append: 附加在後面
# file = open ('e:/test.txt',"a",encoding='utf-8')
# file.write("第一行\n")
# file.write("第二行\n")
# file.close()#如果沒有close，整個檔案會壞掉無法讀取

#with-as :離開區域後，會自動 close file
with open("e:/test.txt",'a',encoding="utf-8") as file:
    file.write("第一行\n")
    file.write("第二行\n")