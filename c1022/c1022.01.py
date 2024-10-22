import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료시켜줌

# print(res.text)

# 태그를 활용한 검색방법
# find, find_all <-> select_one, select

soup = BeautifulSoup(res.text,"lxml")
# print(soup.find("h2",{"class":"rankingnews_tit"}))
# print(soup.select_one('h2.rankingnews_tit').text)

data = soup.select_one("div.rankingnews_box_wrap")
news = data.select("div.rankingnews_box")
for idx,new in enumerate(news):
  print("언론사 이름 : ",new.select_one("strong.rankingnews_name").text)
  news_lists = new.select("ul.rankingnews_list>li")
  for idx,news_list in enumerate(news_lists):
      print(f"{idx+1} : ",news_list.select_one("div.list_content>a").text)

# print(soup.select_one("div#wrap > div.rankingnews _popularWelBase _persist > div#rankingnews_box > strong.rankingnews_name").text)


# #html,css 파싱(정리)이 되어서 출력
# print(soup.prettify())

