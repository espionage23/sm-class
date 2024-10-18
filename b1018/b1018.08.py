class Student:
  count = 0

  # students 딕셔너리 저장
  students = []

  def __str__(self):
    return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}\t"


  def __init__(self,name,kor,eng,math):
    Student.count += 1
    self.no = Student.count
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = (kor+eng+math)/3
    self.rank = 0
    Student.students.append(self)

  
  def title(self):
    return {"no":self.no,"no":self.name,"no":self.kor,"no":self.eng,"no":self.math,"no":self.total,"no":self.avg,"no":self.rank}
  
  #출력
  def stu_print(cls):
    for s in cls.students:
      print(str(s))

# 클래스 - 변수, 함수의 집합체
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수

# 1. 학생성적입력
# 이름, 국어, 여어, 수학 -> 번호, 국어,영어,수학,합계,평균,등수
# 클래스 1개가 생성이 되고
# 클래스의 참조변수(__str__)를 입력해서 출력을 해보세요.

while True:
  print(" [ 학생성적프로그램 ]")
  print(" 1.학생성적입력")
  print(" 2.학생성적출력")
  choice = int(input("원하는 번호 >> "))

  if choice == 1:
    name = input("이름 >>")
    score = []
    for i in range(2,5):
      score.append(int(input(f"{s_title[i]}점수를 입력 >> ")))
    s1 = Student(name,*score)

    for s in Student.students:
      print(s)

  elif choice == 2:
    print(" [ 학생성적출력 ]")
    print(*s_title,sep='\t')
    print("-"*70)
    Student.stu_print()



    