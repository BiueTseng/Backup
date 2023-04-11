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
# pip install beautifulsoup4 lxml

# def getStock(yyyy, mm):
#     #下拉式選單，除了 find_element外，還要用 Select()轉成下拉式物件
#     select=Select(browser.find_element(By.NAME, "yy"))
#     select.select_by_value(str(yyyy))
#     select=Select(browser.find_element(By.NAME,"mm"))
#     select.select_by_value(str(mm))
#     btn=browser.find_element(By.CLASS_NAME,"button")
#     btn.click()
#     try:
#         WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.TAG_NAME,"td")))
#         soup=BeautifulSoup(browser.page_source, 'html.parser')
#         trs=soup.find_all('tr', role='row')
#         ls=[]
#         for i in range(1, len(trs)):
#             tds=trs[i].find_all("td")
#             ds=tds[0].text.split("/")
#             ls.append(
#                 [f'{int(ds[0]) + 1911}-{ds[1]}-{ds[2]}',
#                 float(tds[1].text.replace(",","")),
#                 float(tds[2].text.replace(",","")),
#                 float(tds[3].text.replace(",","")),
#                 float(tds[4].text.replace(",", ""))]
#             )
#     except:
#         pass
#     return ls

def getStock(yyyy,mm):
    #先抓取下拉式方塊，要用Select()去抓取
    select = Select(browser.find_element(By.NAME,"yy"))
    select.select_by_value(str(yyyy))
    select = Select(browser.find_element(By.NAME,"mm"))
    select.select_by_value(str(mm))
    btn = browser.find_element(By.CLASS_NAME,"button")
    btn.click()
    try:
        # WebDriverWait(browser,20).until(EC.presence_of_element_located(By.TAG_NAME,"td"))
        WebDriverWait(browser,20).until(EC.presence_of_element_located((By.TAG_NAME,"td")))
        soup = BeautifulSoup(browser.page_source,'html.parser')
        trs = soup.find_all('tr',role = 'row')
        ls=[]
        #找每一列
        # for tr in trs:
        #     print(tr)
        #找每一行 要跳過第0行的名稱
        for i in range(1,len(trs)):
            tds = trs[i].find_all("td")
            # print(tds)
            ds = tds[0].text.split("/")
            ls.append(
                [f'{int(ds[0])+1911}-{ds[1]}-{ds[2]}',
                float(tds[1].text.replace(",","")),
                float(tds[2].text.replace(",", "")),
                float(tds[3].text.replace(",", "")),
                float(tds[4].text.replace(",", ""))]
            )
    except:
        pass
    return ls

opt = Options()
# opt.add_argument('--headledss')
opt.add_argument('disable-gpu')
opt.add_experimental_option('detach',True)
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service,options =opt)
browser.get("https://www.twse.com.tw/zh/page/trading/indices/MI_5MINS_HIST.html")

yyyy = 2022
conn = mysql.connect(host ="localhost",
                         user = "BiueTseng",
                         password = "BiuELighT-1202",
                         database = "cloud")
cursor = conn.cursor()
cmd = "insert into 台灣股市 (日期, 開盤, 最高, 最低, 收盤) values (%s, %s, %s, %s, %s)"
for mm in range(1,3):
    datas = getStock(yyyy,mm)
    print(f'處理{yyyy}/{mm}月份...')
    cursor.execute(f"delete from 台灣股市 where 日期 like '{yyyy}-{mm:02d}%'")
    conn.commit()
    cursor.executemany(cmd, datas)
    conn.commit()
    time.sleep(random.randint(5, 8) + random.random())
cursor.close()
conn.close()