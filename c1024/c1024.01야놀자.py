from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random

# url = "https://www.yanolja.com/"
# # 브라우저 열기
# browser = webdriver.Chrome()
# # 브라우저 최대화
# browser.maximize_window()
# #url 입력
# browser.get(url)

# # 검색창 클릭
# browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/header/section/a[2]/div/div').click()

# # 날짜
# browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[2]/div[1]/button').click()
# time.sleep(1)
# browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]').click()
# browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]').click()
# browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[4]/button').click()

# # 검색
# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[1]/div/input')
# elem.click()
# browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[1]/div/input').send_keys("강릉 호텔")
# elem.send_keys(Keys.ENTER)

# # 로딩 대기
# # 화면의 호텔검색 내용이 나올때까지 대기, 최대 30초
# WebDriverWait(browser,30).until(lambda x:x.find_element(By.XPATH,'//*[@id="__next"]/div/main/section/div[2]'))

# # 스크롤 내리기
# # excute_script(): 자바스크립트 실행 함수
# prev_height = browser.execute_script('return document.body.scrollHeight')

# while True:
#   browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#   time.sleep(1)
#   # 페이지 로딩되면서 길어진 길이를 다시 가져옴
#   curr_height = browser.execute_script("return document.body.scrollHeight")
#   # 페이지를 스크롤해서 길이가 더 길어졌는지 확인
#   if prev_height == curr_height:
#     break
#   # 길이가 더 길어졌으면, 이전 길이에 현재 길이를 입력시킴
#   prev_height = curr_height

# print("완료")

# # 웹스크래핑--------------------------------
# # html 저장
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('c1024/yanolja.html','w',encoding='utf-8') as f:
#   f.write(soup.prettify())

# 파일 road 후 soup로 파싱
with open('c1024/yanolja.html','r',encoding='utf-8') as f:
  soup = BeautifulSoup(f,'lxml')
# 평점 4.8 이상, 금액 17만원 이하 검색해서 출력

# 1.
# 호텔명:
# 평점:
# 금액:
# -----------------
# 2.
# 호텔명

# 기준점
data = soup.select_one("#__next > div > main > section > div.PlaceListBody_listContainer__2qFG1")
# 호텔 여러개 정보리스트
lists = data.select("div.PlaceListItemText_container__fUIgA")

true_num = 0
fail_num = 0
except_num = 0
search_list=[]

for idx,list in enumerate(lists):
  try:
    rating = list.select_one('span.PlaceListScore_rating__3Glxf').text.strip()
    rating = float(rating)
    price = list.select_one('span.PlacePriceInfoV2_discountPrice__1PuwK').text.strip()
    price = int(price.replace(",",""))
    if rating < 4.8 or price > 180000:
      print(f"{idx+1}번째 조건불충족")
      fail_num += 1
      print("-"*40) 
      continue
    print(f"{idx+1}")
    name = list.select_one('strong.PlaceListTitle_text__2511B').text.strip()
    print(f"호텔명 : ", name)
    print(f"평점 : ", rating)
    print(f"금액 : ", price)
    print("-"*40)
    search_list.append([idx+1,name,rating,price])
    true_num += 1
  except Exception as e:
    print("예외", e)
    except_num += 1

# 리스트에 담고 정렬
# [1,호텔명,평점,가격]
search_list.sort(key = lambda x:x[2],reverse=True)
print(search_list[:5])

# 금액 순차정렬
search_list.sort(key = lambda x:x[3])
print(search_list[:5])


input("Enter 키를 입력하면 완료됩니다.")



