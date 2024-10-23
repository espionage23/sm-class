from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random

# url = "http://www.naver.com"
# # 크롬 브라우저 열기
# browser = webdriver.Chrome()
# # 네이버 페이지 이동
# browser.get(url)
# #로그인버튼 선택
# elem = browser.find_element(By.CLASS_NAME,"MyView-module__link_login___HpHMW")
# # 로그인버튼 클릭
# elem.click()
# time.sleep(random.randint(2,5))

# # 자바스크립트 호출방법
# id = "zalstmd23" #본인 아이디
# pw = "asdf76029657" #본인 패스워드
# input_js = f'document.getElementById("id").value="{id}"; \
# document.getElementById("pw").value="{pw}";'
# browser.execute_script(input_js)
# time.sleep(random.randint(2,5))
# elem = browser.find_element(By.CLASS_NAME,"btn_login")
# elem.click()

# # 완료
# time.sleep(100)
# =-------------------------------------------------------------------------------------

url = "http://www.daum.net"
# 크롬 브라우저 열기
browser = webdriver.Chrome()
# 네이버 페이지 이동
browser.get(url)
#로그인버튼 선택
elem = browser.find_element(By.CLASS_NAME,"btn_login")
# 로그인버튼 클릭
elem.click()
time.sleep(random.randint(2,5))

# 자바스크립트 호출방법
id = "zalstmd23@nate.com" #본인 아이디
pw = "asdf76029657" #본인 패스워드
input_js = f'document.getElementById("loginId--1").value="{id}"; \
document.getElementById("password--2").value="{pw}";'
browser.execute_script(input_js)
time.sleep(random.randint(2,5))
elem = browser.find_element(By.CLASS_NAME,"btn_g")
elem.click()

# 완료
time.sleep(100)
# -------------------------------------------------
# # id 값을 입력
# elem = browser.find_element(By.ID,"id")
# elem.send_keys("zalstmd23")
# time.sleep(random.randint(2,5))
# elem = browser.find_element(By.ID,"pw") 
# elem.send_keys("asdf76029657")
# time.sleep(random.randint(2,5))

# # 로그인 버튼 클릭
# elem = browser.find_element(By.CLASS_NAME,"btn_login")
# elem.click()
