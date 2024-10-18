class Student:
  # 인스턴스 변수 - 객체선언을 하면 변수는 개별적으로 생성
  count = 0  # 클래스 변수 - 모든 객체가 동일한 변수를 사용

  # students 리스트 딕셔너리 저장
  students = []  # 클래스 리스트
  # 클래스 함수
  @classmethod  # 클래스 함수 표시
  def stu_print(cls):
    for s in cls.students:
      print(str(s))

  def __init__(self,name,kor,eng,math):
    Student.count += 1
    self.no = Student.count   #클래스변수 - 공용으로 변수를 사용
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = (kor+eng+math)/3
    self.rank = 0
    # 클래스 리스트에 추가
    Student.students.append(self)

  # 객체를 문자열로 리턴해주는 함수 - 리턴은 문자열이여야만 함
  def __str__(self):
    return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}\t"

  def print(self):
    return {"no":self.no,"name":self.name,"kor":self.kor,"eng":self.eng,"math":self.math,"total":self.total,"avg":self.avg,"rank":self.rank}
  
# #### 프로그램 시작 ######
# s1 = Student()
# s1.students
# s2 = Student()
# s2.students

  
# 클래스 - 변수, 함수의 집합체
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
    
s_t = ["no",'name','kor','eng','math','total','avg','rank']



while True:
  print(" [ 학생성적 프로그램 ]")
  print(" 1. 학생성적입력 ")
  print(" 2. 학생성적출력 ")
  print(" 3. 홍길동, 유관순 비교 ")
  choice = int(input("원하는 번호 >>"))

  if choice == 1:
    name = input("이름을 입력 >>")
    score = []
    for i in range(2,5):
      score.append(int(input(f"{s_title[i]}점수를 입력 >> ")))
    s1 = Student(name,*score)
    # print(s1.students[0])

    # 클래스 변수 접근
    for s in Student.students:
      print(s)

    # 인스턴스 변수 - 참조변수,변수명, 참조변수명.함수명
    # 클래스 변수   - 클래스명.변수명, 클래스명,함수명
    # students.append(Student(name,*score))  # 클래스로 저장
    # students 리스트 딕셔너리 타입으로 변경해서 입력
    # s1 = Student(name,*score)
  elif choice == 2:
    print(" [ 학생성적출력 ]")
    print(*s_title,sep='\t')
    print("-"*80)
    Student.stu_print()
  elif choice == 3:
    s1 = Student("홍길동",100,100,90)
    s2 = Student("유관순",90,100,90)

s1 = Student("홍길동",100,100,99)





# # students 리스트 딕셔너리 저장
# students = []
# s1 = Student("홍길동",100,100,99)
# print(s1)   # 0x000 - > __str__() 정의 된 형태로 출력



# print(s1.print())
# students.append(s1.print())
# s2 = Student("유관순",99,99,98)
# print(s2.print())
# students.append(s2.print())
# print("-"*50)
# print(students)



# s1 = Student("홍길동",100,100,99)
# print(s1.name)
# print("s1 카운트 : ",s1.count)
# s2 = Student("유관순",90,90,99)
# print(s2.name)
# print("s2 카운트 : ",s2.count)
# print("s1 카운트 : ",s1.count)

