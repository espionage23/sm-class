import datetime

member = []
m_keys = ['id','pw','name','nicName','address','money']

#member.txt 파일을 읽기
#member에 저장

# member.txt 파일 읽기, member 딕셔너리 저장
f = open('member.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line: break
  m = line.strip().split(", ")
  m[5] = int(m[5])
  member.append(dict(zip(m_keys,m)))
  print(member)
#----------------------------------------------
cartNo = 0
cart = []
c_keys = ["cno","id","name","pCode","pName","price","date"]
f = open('shop_cart.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line: break
  c = line.strip().split(",")
  c[0] = int(c[0])
  c[5] = int(c[5])
  cart.append(dict(zip(c_keys,c)))
  #---------------------------------------------




product = [
  {"no":1, "pCode":"t001", "pName":"삼성TV", "price":2000000, "color":"black"},
  {"no":2, "pCode":"g001", "pName":"LG냉장고", "price":3000000, "color":"white"},
  {"no":3, "pCode":"h001", "pName":"하만카돈스피커", "price":500000, "color":"gray"},
  {"no":4, "pCode":"w001", "pName":"세탁기", "price":1000000, "color":"yellow"},
]



session_info = {}
p_title = ["번호","아이디","이름","상품코드","상품명","가격","구매일자"]




### 함수선언 ###
def buy(choice,cartNo):
  print(f"{product[choice-1]['pName']} 를 구매하셨습니다.")
  print("구매내역에 등록합니다.")
  print()
  #로그인정보 - session_info
  now = datetime.datetime.now()
  today = now.strftime("%Y-%m-%d %H:%M:%S")
  c = {"cno":cartNo+1, "id":session_info['id'],"name":session_info['name'],"pCode":product[choice-1]['pCode'],"pName":product[choice-1]['pName'],"price":product[choice-1]['price'],"date":today}
  session_info['money'] -= product[choice-1]['price']
  cart.append(c)
  
  cartNo += 1
  return cartNo



# 구매내역 함수
def buy_output():
      # 구매내역 출력
    print(f"{p_title[0]}\t{p_title[1]}\t{p_title[2]}\t{p_title[3]}\t{p_title[4]:15s}\t{p_title[5]}\t{p_title[6]}")
    print("-"*90)
    sum = 0
    for c in cart:
      sum += c['price']
      print(f"{c['cno']}\t{c['id']}\t{c['name']}\t{c['pCode']}\t{c['pName']:15s}\t{c['price']}\t{c['date']}")

    print(f"총 구매 금액 : {sum:,}") 
    print(f"총 구매 건수 : {len(cart)}") 
# 구매내역 함수

#충전 함수
def buy_money():
    input_money = int(input("충전할 금액을 입력 >>"))
    session_info['money'] += input_money
    print(f"현재 금액 :{session_info['money']:,}")



# 저장 함수
def buy_save():
  # member.txt 파일 생성후 csv 형태로
  f = open('member.txt','w',encoding='utf-8')
  for m in member:
    f.write(f"{m['id']}, {m['pw']}, {m['name']}, {m['nicName']}, {m['address']}, {m['money']}\n")
  f.close()
  print("내용 저장이 완료")
  print()
  # cart.txt 파일 생성후 csv 형태로
  f = open('cart.txt','w',encoding='utf-8')
  for c in cart:
    'cno','id','pw','pCode','pName','price','date'
    f.write(f"{c['cno']},{c['id']},{c['name']},{c['pCode']},{c['pName']},{c['price']},{c['date']}\n")
  f.close()
  print("내용 저장이 완료")
  print()


###---------------------------프로그램----------------------------###
while True:
  print("[ 로그인 화면 ]")
  input_id = input("아이디를 입력하세요. >>")
  input_pw = input("비밀번호를 입력하세요. >>")

  #db에서 가져옴.
  #member 데이터를 가지고 비교
  flag = 0
  for m in member:
    if input_id == m['id'] and input_pw == m['pw']:
      print("SM SHOP에 오신것을 환영합니다.")
      session_info = m
      flag = 1
      break #for문에 브레이크
  if flag == 0:
    print("아이디 또는 패스워드가 일치하지 않습니다.")
  else:
    break 

while True:
  print("           [ SM-SHOP ]")
  print(f"                                닉네임:{session_info['nicName']}님 ")
  print(f"                                금액: {session_info['money']:,}원")
  print("1. 삼성TV - 2,000,000")
  print("2. LG냉장고 - 3,000,000")
  print("3. 하만카돈스피커 - 500,000")
  print("4. 세탁기 - 1,000,000")
  print("7. 내용저장")
  print("8. 구매내역")
  print("9. 금액 충전")
  choice = int(input("구매하려는 상품번호를 입력하세요. >>"))

  if choice == 1:
    cartNo = buy(choice,cartNo)  #상품구매 함수호출
  elif choice == 2:
    cartNo = buy(choice,cartNo)  
  elif choice == 3:
    cartNo = buy(choice,cartNo)
  elif choice == 4:
    cartNo = buy(choice,cartNo)
  elif choice == 7:
    buy_save()
  elif choice == 8:
    buy_output()
  elif choice == 9:
    buy_money()

