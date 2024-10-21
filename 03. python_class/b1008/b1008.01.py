students = []
no = 0
while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")
  
  if choice == '1':
    while True:
      print("[학생성적입력]")
      no += 1
      name = input("학생 이름 (취소:0)>>")
      if name == '0':
        print("프로그램 종료")
        break
      kor = int(input("국어 >>"))
      eng = int(input("영어 >>"))
      math = int(input("수학 >>"))
      total = kor+eng+math
      avg = round(total/3,2)
      rank = 0
      print(f"{no}. 이름:{name} 국어:{kor} 영어:{eng} 수학:{math} 합계:{total} 평균:{avg} 등수:{rank}")
      s = [no,name,kor,eng,math,total,avg,rank]
      students.append(s)

  elif choice =='2':
    print("[학생성적출력]")
    #상단헤더
    print("-"*60)
    print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수\t")
    #학생 데이터
    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]}\t{s[7]}\t")
    print("-"*60)

  elif choice == '3':
    print("[학생성적수정]")
    pass
  elif choice == '4':
    print("[학생성적검색]")
    name = input("검색할 학생 이름>>")
    for s in students:
      if s[1] == name:
        print(f"{name} 학생을 찾았음")
        #상단헤더
        print("-"*60)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수\t")
        #학생 데이터
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]}\t{s[7]}\t")
        print("-"*60)
        count = 1
        break

      if s[1] != name:
        print("찾고자 하는 학생이 없습니다. 다시 검색하세요.")
        break

  elif choice == '5':
    print("[학생성적삭제]")
    pass

  elif choice == '6':
    print("[등수처리]")
    pass

  elif choice == '0':
    print("[프로그램 종료]")
    print("프로그램을 종료합니다.")
    break

