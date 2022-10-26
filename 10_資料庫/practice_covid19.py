import mysql.connector as mysql
#建立遠端資料庫連線
conn = mysql.connect(host ="mahaljsp.asuscomm.com",
                     user ="lcc",
                     password ="lcc0507",
                     database ="cloud")
cursor = conn.cursor()
cmd = "select * from covid19 order by cov_date"
cursor.execute(cmd)
rs = cursor.fetchall()
# for r in rs:
#     print(r)
# cursor.close()
# conn.close()
#建立本機資料庫連線
conn = mysql.connect(host="localhost",
                     user ="BiueTseng",
                     password = "BiuELighT-1202",
                     database ="cloud")
#建立執行命令的物件--cursor :游標
cursor = conn.cursor()
#第一種搬運法
# for r in rs:
#     #try:
#         cmd=f"insert into covid19 (cov_date, lng, lat, area, address) values ('{str(r[1])}',{r[2]},{r[3]},'{str(r[4])}','{str(r[5])}')"
#         print(cmd)
#         cursor.execute(cmd)
#         conn.commit()
#     # #except mysql.errors.IntegrityError as e:
#     #     print("日期重複")
# cursor.close()
# conn.close()
#第二種搬運法
data=[]
for r in rs:
    data.append([str(r[1]),r[2],r[3],r[4],r[5]])
print(data)
cmd="insert into covid19 (cov_date,lng,lat,area,address) values (%s,%s,%s,%s,%s)"
cursor.executemany(cmd,data)
conn.commit()
cursor.close()
conn.close()