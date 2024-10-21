import requests
from bs4 import BeautifulSoup

url = 'http://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%98%81%ED%99%94'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# soup 변환
soup = BeautifulSoup(res.text,'lxml')
with open('c1021/screen.html','w',encoding='utf-8') as f:
  f.write(soup.prettify())

data = soup.find('c-flicking',{'id':'mor_history_id_0'})
# screens = data.find("c-doc")
# print("개수 : ",len(screens))

print("순위 :",data.find('c-badge-text').next)
print("제목 :",data.find('c-title').next)
print("예매율 :",data.find("c-contents-desc").next)
print("날짜 :",data.find("c-contents-desc-sub").next)
print('이미지 url : ',data.find('c-thumb')['data-original-src'])
with open('c1021/1.jpg','wb') as f:
  re_img = requests.get({data.find('c-thumb')['data-original-src']})
  f.write(re_img.content)

print('완료')


# print(soup.find('div',{'class':'c-paging'}).find('ul',{'class':'c-list-basic ty_flow35'}).find('c-doc',{'class':'_cubic hydrated'}).text)

# print(soup.find('c-flicking',{'id':'mor_history_id_0'}))
# print(data.find('div',{'class':'item-title'}).text)