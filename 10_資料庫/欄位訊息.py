import mysql.connector as mysql

conn = mysql.connect(host = "mahaljsp.asuscomm.com",
                     user = "lcc",
                     password = "lcc0507",
                     database = "cloud")
cursor = conn.cursor()
cursor.execute("select * from 今彩539")
for d in cursor.description:
    print(d[0])