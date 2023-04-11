#pip install matplotlib
import mysql.connector as mysql
import pylab as plt

conn = mysql.connect(host ="localhost",
                         user = "BiueTseng",
                         password = "BiuELighT-1202",
                         database = "cloud")
cursor = conn.cursor()
cmd = "select * from 台銀黃金 order by 日期 asc"
cursor.execute(cmd)
rs = cursor.fetchall()
datas =[r[1] for r in rs]
y = [r[3] for r in rs]
x = list(range(len(rs)))
cursor.close()
conn.close()

plt.plot(x,y)
f=plt.poly1d(plt.polyfit(x,y,10))

plt.plot(x,f(x),color='red',linewidth=2)
plt.show()