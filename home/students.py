# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
stuNo = len(students)+1  # 학생번호 생성
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수


#학생성적프로그램
while True:
    print("[학생성적프로그램]")
    print("-"*60)
    print("1.학생성적입력")
    print("2.학생성적출력")
    print("3.학생성적수정")
    print("4.학생성적검색")
    print("5.학생성적삭제")
    print("6.학생성적등수")
    print("0.프로그램 종료")
    print("-"*60)
    choice = input("원하는 번호를 입력하세요. (종료:0)>>")

    #1학생성적입력
    if choice == "1":
        print("학생성적입력")
        while True:
            name = input("학생의 이름을 입력하세요.")
            if name == '0':
                print("프로그램 종료")
                break
            
    
    # 2. 학생성적출력
    elif choice == "2":
        print("학생성적출력")
    
    # 3. 학생성적수정
    elif choice == "3":
        print("학생성적수정")
    
    # 4. 학생성적검색
    elif choice == "4":
        print("학생성적검색")
    
    # 5. 학생성적삭제
    elif choice == "5":
        print("학생성적삭제")
    
    # 6. 학생성적등수
    elif choice == "6":
        print("학생성적등수")
    
    # 0. 프로그램 종료
    elif choice == "0":
        print("프로그램 종료")
        print("프로그램을 종료합니다.")
        break