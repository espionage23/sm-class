students = []
no = 1
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']  #전역변수로 뽑기
 
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
      print(f"번호:{no},이름:{name},국어:{kor},영어:{eng},수학:{math},합계:{total},평균:{avg:.2f},등수:{rank}")

      s = [no,name,kor,eng,math,total,avg,rank]
      students.append(s)
      no+=1

  elif choice == '2':
    print("[학생성적 출력]")
    print()

    #상단 출력
    for st in s_title:
      print(st,end="\t")
    print()
    print()

    #학생성적 출력
    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
    print("-"*60)

  elif choice == '3':
    print("[학생성적 수정]")
    # 홍길동, 유관순, 이순신중에 유관순의 학생 성적
    name = input("수정하고자 하는 학생 이름을 입력 (종료:0)>>")
    count = 0
    for s in students:
      if s[1] == name:
        print(f"{name} 학생을 찾았음")
        print("[ 과목선택 ]")
        print("1. 국어점수 ")
        print("2. 영어점수 ")
        print("3. 수학점수 ")
        print("0. 성적수정을 취소합니다. ")
        choice = input("원하는 번호를 입력>>")
        if choice == "1":
          print("현재 국어점수 :",s[2])
          s[2] = int(input("변경할 국어점수 입력 : "))
        elif choice == "2":
          print("현재 국어점수 :",s[3])
          s[3] = int(input("변경할 영어점수 입력 : "))
        elif choice == "3":
          print("현재 국어점수 :",s[4])
          s[4] = int(input("변경할 수학점수 입력 : "))
        elif choice == "0":
          print("성적수정을 취소합니다.")
          count = 1
          
        if choice != "0":
          s[5] = s[2]+s[3]+s[4] #합계 변경
          s[6] = s[5]/3
          print(f"{name} 학생의 성적이 변경되었습니다.")
          count =1

    #없을때
    if count == 0:
      print("수정을 취소합니다.")
      print()

          

  elif choice == '4':
    print("[학생성적 검색]")
    name = input("찾고자 하는 학생 이름을 입력>>")
    #students 10명
    count = 0
    for s in students:
      if s[1] == name:
        print(f"{name} 학생을 찾았음")
        #찾은 학생의 데이터를 출력
        #상단 출력
        for st in s_title:
          print(st,end="\t")
        print()
        print()

        #학생성적 출력
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
        print()
        count = 1
        break
      # else:  #얘로 찾으면 삥삥 돌아서 안돼 그래서 카운터로 해야됨
      #   print("찾고자 하는 학생의 이름이 없습니다.")
      #   print()

    if(count == 0):
      print("찾고자 하는 학생의 이름이 없습니다.")
      print()


  elif choice == '0':
    print("[성적 프로그램 종료]")
    print("프로그램을 종료합니다.")
    break