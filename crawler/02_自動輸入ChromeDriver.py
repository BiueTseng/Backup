# 自動抓取ChromeDriver.exe 相對應的版本
# 當系統更新 Chrome瀏覽器時，我們並不知道，所以也不知要手動更改ChromeDriver.exe的版本
# pip install webdriver-manager  | packaging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

ops = Options()
# opt.add_argument('--headless')
ops.add_argument('--disable-gpu')
# 新版的ChromeDriver會自動關閉，解決方法
# 1. a=input("press any key")
# 2. browser.add_experimental_option('detach',True)
# 讓瀏覽器不會自動關閉，待程式撰寫完成，最好註解
ops.add_experimental_option('detach',True)

# ChromerDriverManager()自動下載Chromedriver.exe
# 下載位置 : C:\User\User\.wdm\drivers\chromedriver\win32\107.x.xxxx.xx\chromedriver.exe
browser = webdriver.Chrome(ChromeDriverManager().install(),options = ops)

browser.get("http://tw.yahoo.com")
# a =  input("Press any key...")