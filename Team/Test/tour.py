from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random

# https://www.modetour.com/

url = "https://www.modetour.com"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=header)
print("코드 상태 :",res.status_code)
res.raise_for_status() #정상코드



# 파일 불러와서 저장하기 - 1회
url = "https://www.modetour.com"
browser = webdriver.Chrome()

# 이동하려는 주소 입력
time.sleep(3)
browser.get(url)
time.sleep(3)
soup = BeautifulSoup(browser.page_source,"lxml")

# 파일 저장하기
with open('Team/b.html','w',encoding='utf-8') as f:
  f.write(soup.prettify())