import requests
from bs4 import BeautifulSoup

url = 'http://www.melon.com/index.htm'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# soup 변환
soup = BeautifulSoup(res.text,'lxml')

print(soup.find('div',{'class':'hot_issue'}).find('ul',{'class':'sub_list'}).find('dl',{'class':'ml0'}))