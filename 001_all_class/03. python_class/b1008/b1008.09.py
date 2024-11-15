
# #학생성적 입력부분을 구현하시오.
# #dict 타입으로 입력을 할 것
# #입력이 완료되면 출력이 바로 되도록 하시오.

# students['no'] = 1
# students['name'] = input("이름을 입력하시오.>>")
# students['kor'] = int(input("국어점수 >>"))
# students['eng'] = int(input("영어점수 >>"))
# students['math'] = int(input("수학점수 >>"))
# students['total'] = students['kor']+students['eng']+students['math']
# students['avg'] = students['total']/3
# students['rank'] = 0

# print(students)


# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수

while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("7. 학생성적정렬")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")

  #입력
  if choice == '1':
    print("[학생성적 입력]")
    while True:  # 얘가 있어야 1번에서 계속 도는거임
      name = input(f"{no}번째 이름을 입력하시오. (종료: 0)")
      if name == '0':
        print("프로그램 종료")
        break
      kor = int(input("국어"))
      eng = int(input("영어"))
      math = int(input("수학"))
      total = kor+eng+math
      avg = (kor+eng+math)/3
      rank = 0
      s = {"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank}
      print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}\t")
      students.append(s)
      stuNo += 1
      print(f"{name} 학생성적이 저장되었습니다.")
      print()


  elif choice == "2":
    print("[학생성적 출력]")
    print()
    #상단헤더
    print("-"*60)
    print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수\t")
    #학생 데이터
    for s in students:
      print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}\t")
    print("-"*60)

  elif choice == "3":
    print("[학생성적 수정]")
  
  elif choice == "4":
    print("[학생성적 검색]")
    name = input("찾으시는 학생의 이름 >>")
    for s in students:
     if s[1] == name:
      print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}\t")

  elif choice == '7':
    print("[학생성적 정렬]")
    print("1.이름으로 순차정렬")
    print("2.이름으로 역순정렬")
    print("3.합계 순차정렬")
    print("4.합계 역순정렬")
    print("5.번호 순차정렬")
    print("0.이전페이지 이동")
    print("-"*60)
    choice = input("원하는 번호 입력 >>")

    if choice == '1':
      students.sort(key=lambda x:x['name'])
    elif choice == '2':
      students.sort(key=lambda x:x['name'],reverse=True)
    elif choice == '0':
      print("이전으로 이동")
      break

    print("정렬이 완료됨")


