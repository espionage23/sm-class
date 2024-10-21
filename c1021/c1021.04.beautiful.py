import requests
from bs4 import BeautifulSoup

url = "https://n.news.naver.com/article/015/0005046720?ntype=RANKING"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
# print(res.text)

with open("c1021/1.html",'w',encoding='utf-8') as f:
  f.write(res.text)

# html,css 정보를 가진 소스 변경
soup = BeautifulSoup(res.text,"lxml") # str -> html태그, css 태그 사용될 수 있는 형태로 변경

# BeautifulSoup 사용해야됨
# 태그 출력, 태그 글자 출력
print(soup.title)  # title 태그
print(soup.title.get_text)    #title 태그 문자열을 출력
# print("없는 태그 :",soup.titletitle)         # 없는 태그 출력시  None
# print("없는 태그 :",soup.titletitle.get_text) # 얘는 에러 발생
# print(" 없는 태그 :", soup.titletitle.text) 없을시 에러 발생
print(soup.a)  # a태그 첫번째 것을 가져옴
print(soup.a.next.text)  #next 타음태그를 가져옴.
print(soup.a.attrs) # 태그의 속성값 가져옴 : 딕셔너리 형태임.
print(soup.a['href'])  #태그의 href 속성값을 가져옴
print(soup.find("div",{"id":"header"}))
print(soup.find("h2",{"class":"rankingnews_tit"}).text) # h2태그 class = "rankingnews_tit"의
print(soup.find_all("div")) #모든 div 태그를 출력
print(len(soup.find_all("div")))  #모든 div 태그 개수 출력
print(type(soup.find_all("div")))


# soup.prettify 정보 저장
with open("c1021/2.html",'w',encoding='utf-8') as f:
  f.write(soup.prettify())
  #soup.prettify() : 소스가 정리되어 저장됨.

print("완료")
