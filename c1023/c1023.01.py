import os
import requests
from bs4 import BeautifulSoup
import time
import csv

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료


soup = BeautifulSoup(res.text,"lxml")

# 기준점
data = soup.select_one("#contentarea > div.box_type_l > table")
stocks = data.select("tr")
# print(len(stocks))


# 1. 상단 타이틀 --------------
# list 생성 1
# sts = stocks[0].select("th")
# st_list = []
# for st in sts:
#   st_list.append(st.text)
# print(st_list)

# list  내포 형식
f = open('c1023/stock.csv','w',encoding='utf-8-sig',newline="")
writer = csv.writer(f)
st_list = [st.text for st in stocks[0].select("th")]
writer.writerow(st_list)
# print(len(st_list))  # 12개
# print(st_list)
#-------------------------------

# 2. 
# print(stocks[1].select("td")) # 항목 1개
# 30개 주식정보를 csv 파일로 저장하시오.

# print(len(stocks)) # 50개
for stock in stocks:
  sts = stock.select("td")
  if len(sts) <=1: continue
  sto_list = [st.text.strip().replace("\t","").replace("\n","") for st in sts]
  writer.writerow(sto_list) #writerow로 해야 리스트 타입을 저장
  # print(sto_list)

f.close()
print("완료")

# print(sto_list)
