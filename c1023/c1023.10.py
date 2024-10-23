#flight.html 금액이 50000원 미만 항공권을 출력하시오.
# 김포 제주 50000원 이하 항공권 개수 : 15개
# 제주 김포 50000원 이하 항공권 개수 : 30개


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random
url = "https://flight.naver.com/"

# 항공권 검색
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
browser.get(url)

# 출발지
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]/b').click()
time.sleep(0.5)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div/div/ul[1]/li[3]/button').click()

# 도착지
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]/b').click()
browser.find_element(By.CLASS_NAME,"autocomplete_input__qbYlb").send_keys("제주")
time.sleep(0.5)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li/a').click()

# 가는 날
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(0.5)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]/button/b').click()
# 오는 날
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[2]').click()
time.sleep(0.5)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[4]/table/tbody/tr[1]/td[7]/button/b').click()

# 인원
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[3]/button[1]').click()
time.sleep(0.5)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]').click()

# 검색
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]').click()
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]').click()

# 화면대기 - 30초동안 대기
# 화면에 찾을려고 하는 html 요소가 있는지 확인
time.sleep(10)


# 화면에 스크롤 내리기
while True:
  prev_height = browser.execute_script("return document.body.scrollHeight")

  # 스크롤 내리기 - 1000
  browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(2) # 다른정보가 추가될때까지 대기
  # 높이 확인 - 2000
  curr_height = browser.execute_script("return document.body.scrollHeight")
  if prev_height == curr_height:
    # 같으면 중지
    break
  prev_height = curr_height


# 데이터 가져와서 처리
# BeautifulSoup 데이터 처리
# 웹스크래핑
soup = BeautifulSoup(browser.page_source,"lxml")
with open('c1023/flight.html','w',encoding='utf-8') as f:
  f. write(soup.prettify())

data = soup.select_one("#__next > div > main > div.domestic_flight_content__vYDHd")
lists = data.select("div.domestic_prices__WBiv_ > div.domestic_item__5CAye > b")
for idx,list in enumerate(lists):
  num = list.select_one("i").text
  num = int(num.replace(",",""))
  if num >= 70000:
    print(f"{idx+1}번쨰 예외")
    continue
  else:
    print(f"{idx+1}.",num)

input("enter 키를 입력하면 프로그램이 종료됩니다.")
browser.quit()