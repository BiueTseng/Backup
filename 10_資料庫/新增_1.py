#一筆一筆寫入，速度慢，效能差
#某筆資料錯誤，但可確保其他資料可寫入
import mysql.connector as mysql

conn = mysql.connect(host = "mahaljsp.asuscomm.com",
                     user = "lcc",
                     password = "lcc0507",
                     database = "cloud")
cursor = conn.cursor()
cmd = "select * from 台灣股市 order by 日期"
cursor.execute(cmd)
rs =cursor.fetchall()
# for r in rs:
#     print(r)
# cursor.close()
# conn.close()

conn = mysql.connect(host = "localhost" ,user ="BiueTseng",password="BiuELighT-1202",database="cloud")
cursor = conn.cursor()
for r in rs:
    #11_例外處理
    try:
        cmd=f"insert into 台灣股市 (日期, 開盤, 最高, 最低, 收盤) values ('{str(r[1])}', {r[2]}, {r[3]}, {r[4]}, {r[5]})"
        print(cmd)
        cursor.execute(cmd)
        conn.commit() # commit後才會真正寫入
    except mysql.errors.IntegrityError as e:
        print("日期重複")
        #print(e.msg)
cursor.close()
conn.close()