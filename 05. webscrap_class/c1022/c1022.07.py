import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.melon.com/chart/index.htm'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료시켜줌

soup = BeautifulSoup(res.text,"lxml")

# 기준점.
data = soup.select_one("#frm > div > table")
lists = data.select("tr")
# 101개

# lists[0] : 상단 타이틀
title = []
tits = lists[0].select("th")
for tit in tits:
  title.append(tit.text.strip())

# 1-100위 리스트 출력
for i in range(1,3):
  # 없는 폴더를 만들어야 할 때
  if not os.path.exists("c1022/melon"):
    os.makedirs("c1022/melon")
  
  # with open(f"c1022/melon/{i}.jpg","wb") as f:
  #   lis = lists[i].select("td")
  #   print("순위 :",lis[1].select_one("span").text)
  #   print("이미지 : ",lis[3].select_one('img')['src'])
  #   img = requests.get(lis[3].select_one('img')['src'])
  #   # f.write(img.content)
  #   songs = lis[5].select('div.ellipsis')
  #   print("제목 : ",songs[0].select_one("a").text,end="" )
  #   singers = songs[1].select_one("a")
  #   if len(singers) != 4:
  #     print(singers[0].text)
  #   else:
  #     print(singers[0].text+"-"+singers[1].text)
  #   print("-"*50)


  # with open(f"c1022/melon/{i}.jpg","wb") as f:
  #   lis = lists[i].select("td")
  #   print("순위 :",lis[1].select_one("span").text)
  #   print("이미지 :",lis[3].select_one("img")['src'])
  #   img = requests.get(lis[3].select_one("img")['src'])
  #   f.write(img.content)
  #   songs = lis[5].select("div.ellipsis")
  #   print("곡정보 :",songs[0].select_one("a").text,end="")
  #   singers = songs[1].select("a")
  #   if len(singers) != 4:
  #     print(singers[0].text)
  #   else:
  #     print(singers[0].text+"-"+singers[1].text)
  #   print("-"*50)
# 뭔 차이인지 확인 ㄱ
