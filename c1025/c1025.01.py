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


# 네이버 -------------------------------------------------------------
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("http://www.naver.com")

# 네이버 쇼핑 검색
elem = browser.find_element(By.ID,'query')
elem.click()
elem.send_keys('네이버 쇼핑')
time.sleep(1)
elem.send_keys(Keys.ENTER)
time.sleep(2)
se = browser.find_element(By.XPATH,'//*[@id="main_pack"]/section[1]/div/div/div[1]/div/div[2]/a')
se.click()

time.sleep(2)

# 새로운 탭으로 이동
browser.switch_to.window(browser.window_handles[1])

elem = browser.find_element(By.XPATH,'//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input')
elem.click()
elem.send_keys('무선마우스')
elem.send_keys(Keys.ENTER)

input("종료 시 엔터 >> ")

