import requests
from bs4 import BeautifulSoup

url = 'https://www.melon.com/chart/index.htm'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료시켜줌

soup = BeautifulSoup(res.text,"lxml")

# 순위, 사진 링크주소, 제목, 가수명 

# 데이터
data = soup.select_one("#frm > div > table")

# 상단타이틀
tits = data.select("th")
# print(tits.selcet_one('div'))
for idx,tit in enumerate(tits):
  print(tit.select_one('div').text,end='\t')
print()

# 곡 정보
lists = data.select('tbody > tr')
for idx, list in enumerate(lists):
  print(list.select_one)