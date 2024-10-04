students = []
no = 1
#입력
while True:
  print("[학생성적프로그램]")
  print("-"*60)
  print("1.학생성적입력")
  print("2.학생성적출력")
  print("3.학생성적수정")
  print("0.프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요. (종료:0)>>")

  if choice == '1':
    print("[학생성적 입력]")
    while True:  #홍길동, 유관순, 이순신
      name = input("이름을 입력하시오. (상위이동:0)")
      if name == '0':
        break
      kor = int(input("국어점수"))
      eng = int(input("영어점수"))
      math = int(input("수학점수"))
      total = kor+eng+math
      avg = (kor+eng+math)/3
      rank = 0
      print(f"번호:{no},이름:{name},국어:{kor},영어:{eng},수학:{math},합계:{total},평균:{(avg):.2f}")
      
      s = [no,name,kor,eng,math,total,avg,rank] #s : list 타입
      students.append(s)

      no+=1
  elif choice == '2':
    print("[학생성적 출력]")
    print()
    # 출력
    s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']

    #상단출력
    for s in s_title:
      print(s,end="\t")
    print(); print("-"*60)

    #학생성적출력
    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")    #소수점으로 인해 공간 관리를 위해 f 함수로 출력
      print()
    print()
  elif choice == '3':
    print("[학생성적 수정]")
    print()
  elif choice == '0':
    print("[프로그램 종료]")
    print("프로그램 종료합니다.")
    break
    



#이름, 국어, 영어, 수학을 입력 받아서 -> 번호, 이름, 국어, 영어, 수학, 합계, 평균
#이름 0 입력하면 프로그램을 종료합니다. 출력
# no = 1
# while True:  #홍길동, 유관순, 이순신
#   name = input("이름을 입력하시오. (종료:0)")
#   if name == '0':
#     break
#   kor = int(input("국어점수"))
#   eng = int(input("영어점수"))
#   math = int(input("수학점수"))
#   total = kor+eng+math
#   avg = (kor+eng+math)/3
#   print(f"번호:{no},이름:{name},국어:{kor},영어:{eng},수학:{math},합계:{total},평균:{(avg):.2f}")
  
#   s = [no,name,kor,eng,math,total,avg] #s : list 타입
#   s_list.append(s_list)

#   no+=1

# print("프로그램을 종료합니다.")
# print(s_list)