#pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from webdriver_manager.chrome import ChromeDriverManager
ops = Options()
ops.add_argument('--disable-gpu')
# Edge webdriver 瀏覽器開啟方法
# browser = webdriver.Edge()
# browser.get("http://tw.yahoo.com")

browser = webdriver.Chrome('chromedriver.exe',options = ops)
browser.get("https://www.youtube.com")
# browser.get("http://localhost/web/99_table.html")
WebDriverWait(browser,20,0.5).until(EC.presence_of_element_located((By.TAG_NAME,'div')))

print(browser.page_source)
# a = input("press any key...")
