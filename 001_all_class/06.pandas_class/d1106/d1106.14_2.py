from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
import csv
from bs4 import BeautifulSoup

# # 웹 스프래핑 ##
# for i in range(4):
#   # 파일 불러와서 저장하기 - 1회
#   url = f"https://search.daum.net/search?w=tot&q=202{i}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
#   browser = webdriver.Chrome()

#   # 이동하려는 주소 입력
#   browser.get(url)
#   time.sleep(3)
#   soup = BeautifulSoup(browser.page_source,"lxml")

#   # 파일 저장하기
#   with open(f'movie 202{i}.html','w',encoding='utf-8')as f:
#     f.write(soup.prettify())
# # 웹 스프래핑 ##

# -------------------------------------------

# 파일 불러오기 - BeautifulSoup 으로 파싱
for i in range(4):
  with open(f'd1106/movie 202{i}.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')

#기준점
data = soup.select_one('#mor_history_id_0 > div > div.flipsnap_view > div > div:nth-child(1) > c-flicking-item > c-layout > div > c-list-doc > ul')
lists = data.select('li')
print(len(lists))

# for list in lists:
#   print("제목 :", list.select_one('c-title > strong > a').text.strip())
#   print("관객수 :",list.select_one('c-contents-desc > p > a').text.strip())
#   print("날짜 :",list.select_one('c-contents-desc-sub > span').text.strip())
#   # print("이미지 url:",data.select_one('div.item-thumb > c-thumb > div')['data-original-src'])
#   print("-"*60)

















