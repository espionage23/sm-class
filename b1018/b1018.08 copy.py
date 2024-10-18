#클래스 생성
class Student:
  # 1. 생성자 정의가 없음
  # 기본생성자

  # 변수 2종류
  # 인스턴스 변수 : 객체선언할때 만들어짐. 각각의 객체마다 변수가 생성됨.
  # - 참조변수명. 변수명
  # 클래스 변수 : 객체가 선언되지 않아도 만들어짐. 모든 객체가 공통으로 사용함.
  # - 클래스명. 변수명
  # 지역변수 : 함수내에 선언된 변수. 함수가 종료되면 사라짐.

  # 함수 2종류
  # 인스턴스 함수 : 객체선언할때 만들어짐. 각각의 객체마다 함수가 생성됨. 따로따로 노는거임
  # - 참조변수명. 함수명
  # 클래스 함수 : 객체가 선언되지 않아도 만들어짐. 모든객체가 공통으로 함수를 사용함
  # - 클래스명. 함수명
  #@classmethod # 클래스 함수 표시

  # 객체선언 한 참조변수를 출력하면 -> 주소값이 출력됨.
  # - 참조변수를 출력해서 원하는 데이터를 출력하려면, __str__() 함수를 사용해야함.


  # kor = 100  # 클래스 변수 - 클래스명.변수명
  count = 1
  students = []

  @classmethod
  def stu_print(cls):
    for s in cls.students:
      print(str(s))

  def __init__(self,name,kor,eng,math):
    self.no = Student.count#인스턴스 변수 - 참조변수명.변수명
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    Student.count +=1
    Student.students.append(self)

  def __str__(self):
    return f'{self.no},{self.name},{self.kor},{self.eng},{self.math}'   # 리턴값은 문자열이여야만 함.

  # no getter를 사용하지 않으면 접근 불가
  def get_no(self):
    return self.no
  def set_no(self,no):
    if no<0: raise "0 이하는 입력을 할 수 없습니다."
    self.no = no
  
s1 = Student("홍길동",100,100,100)
print(s1)
s2 = Student("유관순",90,90,90)
print(s2)
s3 = Student("강감찬",80,80,80)
print(s3)
s4 = Student("이순신",70,70,70)
print(s4)
print("-"*40)
# 클래스 __str__
Student.stu_print()

#Student.students 리스트
for s in Student.students:
  print(s)

# s1 = Student()
# # s1.no = -100
# s1.set_no(100)
# print(s1.get_no())



# # 객체선언
# # 참조변수명 = 클래스명()
# print("최초 :",Student.kor)

# s1 = Student(10)
# s1.no = 10
# print(s1.no)
# Student.kor = 50

# s2 = Student(20)
# print("s2:",s2.no)

# print("최종 :",Student.kor)