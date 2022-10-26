import mysql.connector as mysql
#建立遠端連線
conn = mysql.connect(host = "mahaljsp.asuscomm.com",
                       user = "lcc",
                       password = "lcc0507",
                       database = "cloud")
#建立執行命令的物件 - :游標
cursor = conn.cursor()
cmd = "select * from 台銀黃金 order by 日期"
cursor.execute(cmd)
rs = cursor.fetchall() #recordSet
# for r in rs:
#     print(r)
#cursor.close()
#conn.close

#建立主機連線
conn = mysql.connect(host ="localhost",
                         user = "BiueTseng",
                         password = "BiuELighT-1202",
                         database = "cloud")
#建立執行命令的物件--cursor :游標
cursor = conn.cursor()
#第一種搬運法
# for r in rs:
#     #11_例外處理
#     try:
#         cmd=f"insert into 台銀黃金 (日期, 買進, 賣出) values ('{str(r[1])}', {r[2]}, {r[3]})"
#         print(cmd)
#         cursor.execute(cmd)
#         conn.commit()
#     except mysql.errors.IntegrityError as e:
#         print("日期重複")
# cursor.close()
# conn.close()
#第二種搬運法

data=[]
for r in rs:
    data.append([str(r[1]),r[2],r[3]])
#print(data)
cmd ="insert into 台銀黃金 (日期,買進,賣出) values (%s,%s,%s)"
cursor.executemany(cmd,data) #只開一次連線，然後將所有資料一次性寫入
conn.commit()
cursor.close()
conn.close()