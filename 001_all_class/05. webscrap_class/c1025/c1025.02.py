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
import pyautogui
import csv


# csv 파일 저장

# browser = webdriver.Chrome()
# browser.maximize_window()
# for i in range(1,6):
#   url = f"https://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list"
#   browser.get(url)
#   soup = BeautifulSoup(browser.page_source,'lxml')
#   # 스크롤 내리기
#   prev_height = browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#   while True:
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(1)
#     # 페이지 로딩되면서 길어진 길이를 다시 가져옴
#     curr_height = browser.execute_script("return document.body.scrollHeight")
#     # 페이지를 스크롤해서 길이가 더 길어졌는지 확인
#     if prev_height == curr_height:
#       break
#     # 길이가 더 길어졌으면, 이전 길이에 현재 길이를 입력시킴
#     prev_height = curr_height
#   with open(f'c1025/naver_shop{i}.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

# 파일 불러오기
# for i in range(1,6):
with open(f'c1025/naver_shop1.html','r',encoding='utf-8') as f:
  soup = BeautifulSoup(f,'lxml')

# 제목, 금액, 평점, 평가수, 찜 정보를 1-5페이까지 가져와서 
# 평점 4.8 이상, 평가수 1000명 이상 인 상품을 csv 파일로 저장하고 출력하시오.

data = soup.select_one('#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx')
pros = data.select('div.product_item__MDtDF')
# pros = data.select('div.adProduct_item__1zC9h') + data.select('div.product_item__MDtDF')
# pros = data.select('div.product_item__MDtDF')
print(len(pros))
c1 = pros[0]['class']
print(c1[0])

# for idx,pro in enumerate(pros):
#   print(idx,".")
#   if pro['class'][0] == 'adProduct_item__1zC9h':
#     title = pro[0].select_one('div.adProduct_info_area__dTSZf > div.adProduct_title__amInq > a').text.strip()
#   else:
#     print('product_item__MDtDF')
#     title = pro[0].select_one('div.product_inner__gr8QR > div.product_info_area__xxCTi > div.product_title__Mmw2K > a').text.strip()



#==============================================================================================================
for idx,pro in enumerate(pros):
  price = pro.select_one('span.price_num__S2p_v > em').text.strip()
  price = int(price.replace(",",""))
  rating = pro.select_one('span.product_grade__IzyU3').text.replace("별점","").strip()
  rating = float(rating)
  num = pro.select_one('em.product_num__fafe5').text.strip()
  num = int(num.replace(",",""))
  print(f"{idx+1}.")
  print("이름 :",pro.select_one('div.product_title__Mmw2K').text.strip())
  print("금액 :",price,"원")
  print("평점 :",rating)
  p_num = pro.select_one('div.product_etc_box__ElfVA > a > em').text.replace('\n','').replace(',','')
  print("평가수 :",p_num)
  print("찜 :",num)


input("엔터 >>")