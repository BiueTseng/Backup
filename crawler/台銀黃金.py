import time, random
from bs4 import BeautifulSoup
import mysql.connector as mysql
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def getData(yyyy,mm):
    browser.get(f"https://rate.bot.com.tw/gold/chart/{yyyy}-{mm:02d}/TWD/1")
    ls=[]
    try:
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        trs = soup.find_all(("tr"))
        # 找每一列
        # for tr in trs:
        #     print(tr)
        for i in range(1,len(trs)):
            tds = trs[i].find_all("td")
            ls.append([
                tds[0].text,
                int(tds[3].text.replace(",","")),
                int(tds[4].text.replace(",", ""))
            ])
    except:
        pass
    return ls


opt = Options()
# opt.add_argument('--headledss')
opt.add_argument('disable-gpu')
opt.add_experimental_option('detach',True)
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service,options =opt)
# datas=getData(2022,11)
# print(datas)
yyyy = 2022

conn = mysql.connect(host ="localhost",
                         user = "BiueTseng",
                         password = "BiuELighT-1202",
                         database = "cloud")
cursor = conn.cursor()
cmd = "insert into 台銀黃金 (日期, 買進, 賣出) values (%s, %s, %s)"
for mm in range(1,12):
    datas = getData(yyyy,mm)
    print(f'處理{yyyy}/{mm}月份...')
    cursor.execute(f"delete from 台銀黃金 where 日期 like '{yyyy}-{mm:02d}%'")
    conn.commit()
    cursor.executemany(cmd, datas)
    conn.commit()
    time.sleep(random.randint(5, 8) + random.random())
cursor.close()
conn.close()

