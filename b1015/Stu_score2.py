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

### --------------------------- 함수 --------------------------- ###

# 1. 학생성적입력 함수
def stu_input(stuNo):
  while True:
    print("[ 학생성적입력 ]")
    no = stuNo + 1
    name = input(f"{no}번째 학생 이름을 기재 | 0. 이전화면으로 이동 >>")
    if name == "0":
      print("이전화면으로 이동")
      break
    kor = int(input("국어점수 >>"))
    eng = int(input("영어점수 >>"))
    math = int(input("수학점수 >>"))
    total = kor+eng+math
    avg = total/3
    rank = 0
    s = {"no":no, "name":name, "kor":kor,"eng":eng,"math":math,"total":total, "avg":avg, "rank":rank}
    students.append(s)
    stuNo += 1
    print(f"{name} 학생의 데이터가 저장되었습니다.")
# 1. 학생성적입력 함수 끝

# 2. 학생성적출력 함수
def stu_output(students):
  print("[ 학생성적출력 ]")
  print()

  #상단출력
  for st in s_title:
    print(st, end="\t")
  print()
  print("-"*60)

  #데이터 load
  for s in students:
    print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
  print()
# 2. 학생성적출력 함수 끝

# 4. 학생성적검색 함수
def stu_search(students):
  while True:
    print("[ 학생성적검색 ]")
    print()
    name = input("찾으시는 학생의 이름 | 0. 이전화면 이동 >>")
    if name == "0":
      print("이전화면 이동")
      break 
    for s in students:
      if name == s['name']:
        #상단출력
        for st in s_title:
          print(st, end="\t")
        print()
        print("-"*60)

        #데이터 load
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()
# 4. 학생성적검색 함수 끝



### -------------------------- 함수 끝 -------------------------- ###

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



###--------------------------- 프로그램 ---------------------------###
  if choice == "1":  # 학생성적입력
    stu_input(stuNo)

  if choice == "2": #학생성적출력
    stu_output(students)

  if choice == "3": #학생성적수정
    print("[ 학생성적수정 ]")
    print()

    for s in students:
      name = input("수정할 학생의 이름 >>")
      print(f"{name} 학생의 수정할 과목")
      print("1. 국어점수")
      print("2. 영어점수")
      print("3. 수학점수")
      choice = input("수정할 과목 선택 >>")
      if choice == "1":
        print(f"현재 국어점수 : {s['kor']}")



  if choice == "4":  #학생성적검색
    stu_search(students)

  if choice == "5":  #학생성적삭제
    pass

  if choice == "6":  #성적등수처리
    pass

  if choice == "7":  #성적등수정렬
    pass

  if choice == "0":
    print("[ 프로그램 종료] ")
    break
