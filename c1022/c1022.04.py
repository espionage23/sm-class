import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/lastsearch2.naver'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료시켜줌

soup = BeautifulSoup(res.text,"lxml")

# 데이터
data = soup.select_one("#contentarea > div.box_type_l > table")

# 상단 타이틀
tits = data.select("tr.type1>th")
for tit in tits:
  print(tit.text,end='\t')
print()
print("-"*100)

# 주식
print(data.select_one("tr").next_sibling.next_sibling.next_sibling.next_sibling)


