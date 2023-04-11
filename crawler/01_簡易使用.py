# pip install selenium
# 下載跟 Chrome 相同版本的 ChromeDriver(chromedriver_win32.zip), https://chromedriver.chromium.org/
# ChromeDriver :類似一個瀏覽器，但功能比 Chrome 更強
# selenium : Python 與 Chrome 溝通的語言
# Chrome :版本 107.0.5304.107 (正式版本) (64 位元)
# 若ChromeDriver 選錯版本，就會無法執行，會出錯
# 下載至crawler專案底下


'''
Linux Server ubuntu/樹梅派的人 : Server沒有圖形介面

內容待老師分享

'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#底下這三段加入，是擷取網頁JavaScript呈現資料必須加入的
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# 動態爬蟲:等候網站 javascript作業執行完。 EC 這一段要手動輸入
from selenium.webdriver.support import expected_conditions as EC
ops = Options()

#底下這段待程式碼撰寫完在開啟
# ops.add_argument('--headless')#無頭模式，沒有視窗
ops.add_argument('--disable-gpu')#也可以註解，預設啟用GPU
browser = webdriver.Chrome('chromedriver.exe',options=ops)
# browser.get("http://tw.yahoo.com")
# browser.get("http://localhost/web/99.php")
browser.get("http://localhost/web/99_table.html")
try:
    #什麼時候需要 Wait : 使用 JavaScript 或 AJAX 產生的資料，就需要 Wait
    #(By.TAG_NAME,'td')是tuple格式
    #預設為每500ms檢查一次，若超過20秒都沒結果，就跑 except
    #WebDriverWait(browser,20(等待秒數),0.1 (每0.1秒 = 100ms 檢查一次，預設為0.5))
    #每有WebDriverWait的話，直接抓取瀏覽器的 輸入層(接收層) 資料。若有等待，則抓取 渲染層 的資料
    WebDriverWait(browser,20,0.5).until(EC.presence_of_element_located((By.TAG_NAME,'td')))
except:
    print("連線錯誤")

print(browser.page_source)

#讓瀏覽器不要自動關閉
a = input("請按任何按鍵...")