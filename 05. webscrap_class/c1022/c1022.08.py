import os
import requests
from bs4 import BeautifulSoup
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

# print(res.text)

soup = BeautifulSoup(res.text,"lxml")

# 제목, 금액, 평점, 평가수, 링크주소, 이미지 주소 

# 기준점
data = soup.select_one("#productList")
# 금액 : 90만원 이상, 평점 4.5 이상, 평가수 500명 이상 만 출력
lists = data.select("li")
n_lists = []
for idx,list in enumerate(lists):
  n_list = [] #제목, 금액, 평점, 평가수, 링크, 이미지
  try:
    price = int(list.select_one("div.price > em > strong").text.replace(",",""))
    rating = float(list.select_one("span.star > em").text)
    num = int(list.select_one("span.rating-total-count").text[1:-1])
    if price >= 900000 and rating >= 4.5 and num >= 500:
      print(f"[{idx} 번째]")
      print("제목 : ",list.select_one("div.descriptions-inner > div.name").text)
      print("금액 : ",price,"원")
      print("평점 : ",rating)
      print("평가수 : ",num)
      print("링크주소 : ","https://www.coupang.com/"+list.select_one("a")['href'])
      print("이미지 :","https:/"+list.select_one("dt.image>img")['src'][1:])
    else:
      print(f"{idx}번째 제외")
  except Exception as e:
    print("에러",e)

while True:
  print("[ 노트북 비교 ]")
  print("1.금액정렬")
  print("2.금액역순정렬")
  print("3.평점정렬")
  print("4.평점역순정렬")
  print("0.종료")
  print("-"*50)
  choice = input("원하는 번호 >>")

  if choice == "1":
    # n_lists.sort()
    pass
  elif choice == "2":
    pass
  elif choice == "3":
    pass
  elif choice == "4":
    pass
  elif choice == "0":
    pass

