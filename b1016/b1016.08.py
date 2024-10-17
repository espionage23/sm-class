member = []
cart = []
m_keys = ['id','pw','name','nicName','adress','money']
c_keys = ['cartNo','name','pCode','pName','price','date']


# csv 전환후 딕셔너리
f = open('member.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line : break
  m = line.strip().split(",")
  m[5] = int(m[5])
  member.append(dict(zip(m_keys,m)))
  # print(line.strip())
print(member)
#------------------------------------
cartNo = 0
cart = []
# f = open('cart.txt','w',encoding='utf-8')
# while True:
#   line = f.readline()
#   if not line: break
#   c = line.strip().split(",")
#   c[0] = int(c[0])
#   c[5] = int(c[5])
#   cart.append(dict(zip(c_keys,c)))




product = [
  {"no":1, "pCode":"t001", "pName":"삼성TV", "price":2000000, "color":"black"},
  {"no":2, "pCode":"g001", "pName":"LG냉장고", "price":3000000, "color":"white"},
  {"no":3, "pCode":"h001", "pName":"하만카돈스피커", "price":500000, "color":"gray"},
  {"no":4, "pCode":"w001", "pName":"세탁기", "price":1000000, "color":"yellow"}
]

session_info = {}
p_title = ["번호","아이디","이름","상품코드","상품명","가격","구매일자"]


### -------- 함수 선언 -----------###
### -------- 함수 선언 끝-----------###


#### ----------- 프로그램 -------------- ###
print(" [ /SM Mall ]")

# 로그인
input_id = input("아이디 >>")
input_pw = input("비밀번호 >>")
while True:
  for m in member:
    flag = 0
    if input_id == m['id'] and input_pw == m['pw']:
      print(" SM Mall에 오신것을 환영합니다.")
      session_info = m
      flag = 1
      break
  if flag == 0:
    print("아이디 혹은 비밀번호가 일치하지 않습니다.")
  else:break

while True:
  print("                    [ SM Mall 프로그램 ]")
  print(f"                                             보유 금액:{session_info['money']}")
  print(f"                                             닉네임:{session_info['nicName']}")
  print("1. 삼성TV - 2,000,000")
  print("2. LG냉장고 - 3,000,000")
  print("3. 하만카돈스피커 - 500,000")
  print("4. 세탁기 - 1,000,000")
  print("7. 내용저장")
  print("8. 구매내역")
  print("9. 금액 충전")
  choice = int(input("구매하려는 상품번호를 입력하세요. >>"))

  if choice == 1:
    print(f"{product[choice-1]['pName']} 룰 구매하셨습니다.")
    print("구매내역에 저장합니다.")
    print()
    #로그인 정보 - session_info
    c = {"cno":cartNo+1, "id":session_info['id'],"name":session_info['name'],"pCode":product[choice-1]['pCode'],"pName":product[choice-1]['pName'],"price":product[choice-1]['price']}
    session_info['money'] = product['choice']

    

#### ----------- 프로그램 끝 -------------- ###