import requests
from bs4 import BeautifulSoup

url = 'http://finance.naver.com/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료시켜줌

soup = BeautifulSoup(res.text,"lxml")
sum = 0
#기준점
data = soup.select_one("#container > div.aside > div > div.aside_area.aside_popular")
print(data.select_one("span").text)
pops = data.select("tbody>tr")
# print(len(pops))
for idx,pop in enumerate(pops):
  print(f"{idx+1}.", "회사명 : ",pop.select_one('a').text)
  print("금액 : ",pop.select_one('td').text)
  #합계를 구하시오.
  sum += int(pop.select_one('td').text.replace(",",""))
  
  sps = pop.select_one("td").find_next_sibling("td").select("span")
  tit = ['변동','변동액']
  for idx,sp in enumerate(sps):
    print(tit[idx],":",sp.text.strip())
  print()

print(f"합계 : {sum:,}")

  # next_sibling : 형제관계, find_next_sibling : 형제관계중 검색
  # print("변동 :",pop.select_one('span').text)
  # print("변동금액 :",pop.select_one('span').next.next.next.text.strip())
