import requests
from bs4 import BeautifulSoup

url = 'https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# soup 변환
soup = BeautifulSoup(res.text,'lxml')

# 제목 출력
# print(soup.find('div',{'id':'bestPrdList'}).find('div',{'class':'pname'}).p.text)

# 제목 전부 출력  (자력)
pLists = soup.find('div',{'id':'bestPrdList'}).find_all('li',{'class':'pname'})
res.raise_for_status()
for i,pList in enumerate(pLists):
  print(f"{i+1}.{pList.p.text}\t")
  print(pList.find('div',{'class':'price_info cfix'}).find('span',{'class':'price_detail'}.s.text))
  