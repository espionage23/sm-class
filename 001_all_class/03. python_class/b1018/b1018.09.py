# Student 클래스 생성 후
# 데이터를 직접 입력을 받아, 클래스 선언후 저장
# 번호는 자동으로 부여, 이름, 국어, 영어, 수학, 합계, 평균, 등수
# 클래스 전체 출력
# 클래스 수정

# [ 학생 성적프로그램]
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적수정

class Student:
  students = []
  count = 0
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

  def __str__(self):
    return f'{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}'
  
  def print(self):
    return {"no":self.no,"name":self.name,"kor":self.kor,"eng":self.eng,"math":self.math,"total":self.total,"avg":self.avg,"rank":self.rank}
  
  @classmethod
  def stu_print(self):
    for s in Student.students:
      print(s)
  
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
  print(" [학생성적 프로그램 ]")
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  choice = int(input("원하는 번호 >>"))

  if choice == 1:
    name = input("이름 >>")
    score = []
    for i in range(2,5):
      score.append(int(input(f"{s_title[i]}점수 >>")))
    Student(name,*score)
  elif choice == 2:
    print(" [ 학생성적출력 ]")
    print("-"*70)
    Student.stu_print()