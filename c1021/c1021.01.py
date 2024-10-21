# 웹스크레핑 세팅
import requests
# res = requests.get("http://www.google.com/")  #html 소스를 가져옴.
res = requests.get("http://www.naver.com/")  #html 소스를 가져옴.
# res = requests.get("http://www.melon.com/index.htm")  #html 소스를 가져옴.
res.raise_for_status() # 에러시 종료시켜줌
print(res.text) #htnl 소스 출력

# requests 정보를 가져올시 제이쿼리, 자바스크립트, 외부페이지,react,vue...는 못가져옴. 비동기식으로 작동되는 소스들이기 때문

print("총 문자 길이 : ",len(res.text))

# 웹 소스코드 파일 저장
# f = open("a.html","w",encoding="utf-8")
# f.write(res.text)
# f.close()

# f.close()를 안하는 방법
with open("c1021/naver.html","w",encoding="utf-8") as f:
  f.write(res.text)


# if res.status_code == 200:
#   print(res.text)
# else:
#   print("접근할 수 없음.")

# print("응답 코드 :",res.status_code)  # html 응답코드 200 = 성공   406 = 
# print(res.text)