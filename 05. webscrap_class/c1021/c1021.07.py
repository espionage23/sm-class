import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)

soup = BeautifulSoup(res.text,'lxml')
newLists = soup.find("div",{"class":"rankingnews_box_wrap"}).find_all("div",{"class":"rankingnews_box"})

# 12번 반복
print("개수 :",len(newLists))

for idx,newList in enumerate(newLists):
  print("-"*60)
  print(f"{idx+1}. 타이틀:",newList.find('strong',{'class':'rankingnews_name'}).text)
  ranks = newList.find("ul",{"class":"rankingnews_list"})

  tlists = ranks.find_all('li')
  for i,t in enumerate(tlists):
    print(i+1,":",t.find("a").text)
    

# print(soup.find('div',{'class':'rankingnews_box'}))