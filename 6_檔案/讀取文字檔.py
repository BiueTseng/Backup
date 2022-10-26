#'r' : read only
#'w' : write only
file = open("e:/test.txt",'r',encoding = "utf-8")
#讀取整個檔案，如果檔案非常大，可能記憶體不足，或讀取速度非常慢
#l=file.read()
#print(l)

#讀取指定的大小
# while True:
#     l=file.read(20)#讀取20個字
#     if not l:break
#     print(l,end='')

# line = file.readline().strip() #strip :刪除 "\n"
while True:
    line = file.readline()
    if not line :break
    line = line.strip()#刪除 "\n" 預防第二次輸入空白鍵
    print(line)