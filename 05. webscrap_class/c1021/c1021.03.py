# naver 파일 저장  리솜리조트 파일저장
import requests

url = [
  "http://www.coupang.com/",
  "http://www.naver.com/",
  "http://www.melon.com/",
  "http://www.daum.net/"

]
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}

for i in range(len(url)):
  res = requests.get(url[i],headers=headers)
  res.raise_for_status()
  print("코드 상태 : ",res.status_code)

  with open(f'c1021/{i+1}.html','w',encoding='utf-8') as f:
    f.write(res.text)

print("프로그램 종료")