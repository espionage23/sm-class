from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")



# # 노트북 검색 된 사이트 1,2,3 페이지에서 만족도가 95 이상이면서, 평가수 100 이상, 금액 1500000원 이하 검색하시오.
for i in range(3):
  url = f"https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=53&p={i+1}"
  # 웹
  browser = webdriver.Chrome(options = options)
  browser.maximize_window()
  browser.get(url)
  time.sleep(2)
  soup = BeautifulSoup(browser.page_source,'lxml')
  with open(f'c1024/gmarket{i+1}.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())

# 파일 불러오기
for i in range(3):
  with open(f'c1024/gmarket{i+1}.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')

browser.get_screenshot_as_file("gmk.png")
input("엔터 >>")

data = soup.select_one('#section__inner-content-body-container > div:nth-child(4)')
data_lists = data.select('div.box__item-container')

for idx,list in enumerate(data_lists):
  print(f"{idx+1}.")
  brand = list.select_one('span.text__brand')
  print(f"제품 브랜드 : ",brand)
  name = list.select_one('span.text__item')
  print(f"제품 브랜드 : ",name)