import mysql.connector as mysql

conn = mysql.connect(host = "mahaljsp.asuscomm.com",
                     user = "lcc",
                     password = "lcc0507",
                     database = "cloud")
cursor = conn.cursor()
cmd = "select * from fruit order by 日期"
cursor.execute(cmd)
rs = cursor.fetchall()
# for r in rs:
#     print(r)
# cursor.close()
# conn.close()
#建立主機資料庫連線
conn = mysql.connect(host ="localhost",
                     user = "BiueTseng",
                     password ="BiuELighT-1202",
                     database = "cloud")
cursor = conn.cursor()

# #第一種搬運法
# for r in rs:
#     cmd=f"insert into fruit (日期,國家,水果,數量,單價) values ('{str(r[1])}','{str(r[2])}','{str(r[3])}',{r[4]},{r[5]})"
#     print(cmd)
#     cursor.execute(cmd)
#     conn.commit()
# cursor.close()
# conn.close()

#第二種搬運法
data=[]
for r in rs:
    data.append([str(r[1]),r[2],r[3],r[4],r[5]])
print(data)
cmd="insert into fruit (日期,國家,水果,數量,單價) values (%s,%s,%s,%s,%s)"
cursor.executemany(cmd, data)
conn.commit()
cursor.close()
conn.close()