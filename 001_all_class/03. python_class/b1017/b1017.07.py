
# member 딕셔너리 저장
members = []
m_title = ['id','pw','name','nicName','address','money']

# 파일 불러오기
f = open('b1017/member.csv','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line : break
  # m 리스트 저장
  m = line.strip().split(",") 
  m[5] = int(m[5])
  # m 리스트에 딕셔너리 저장
  members.append(dict(zip(m_title,m)))
f.close() 

while True:
  print("1.회원등록")
  print("2.회원검색")
  choice = input("원하는 번호 >>")
  if choice == "1":
    id = input("ID를 입력하세요. >>")
    flag = 0
    for m in members:
      if m['id'] == id:
        print(f"{id}는 동일한 아이디가 있습니다. 다시 입력하세요.")
        flag = 1
        break
    if flag == 1:
      continue
    else:
      print(f"{id}는(은) 사용가능합니다.")  
      print()
    pw = input("pw를 입력하세요. >>")
    name = input("이름을 입력하세요. >>")
    nicName = input("닉네임을 입력하세요. >>")
    money = int(input("충전금액을 입력하세요. >>"))
    m_list = [id,pw,name,nicName,money]
    members.append(dict(zip(m_title,m_list)))
    print(f"{id}님 회원가입이 완료되었습니다.")
    print(m_list)
    print("-"*50)
    print(members)

  elif choice == "2":
    #  아이디 조회
    search_id = input("찾으시는 아이디를 입력하시오.")
    flag = 0
    for i in members:
      if search_id in i['id']:
        print(f"{i['id']}")
        flag = 1
      
    if flag == 0:
      print("회원을 찾지 못함.")
    else:
      print("총 검색된 인원 :",len(i))






#아이디 검색
# member 리스트에서 입력한 문자로 검색된 데이터를 모두 출력하시오.
# a가 들어가 있는 아이디를 출력