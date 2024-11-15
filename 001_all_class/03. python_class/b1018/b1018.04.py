# 일반적으로 형태의 프록르ㅐㅁ 구현.

# 반지름을 입력받아, 원의 둘레와 넓이를 출력하시오.

# length = int(input("반지름 >>"))
# print("넓이 :",3.14*length**2)
# print("둘레 :", 3.14*2*length)

# 클래스 생성
class Circle:
  def __init__(self,length):
    self.__length = length  # 변수 직접접근 제한 __ 이걸로
    length = 0
  
  # 원의 넓이
  def get_area(self):
    return 3.14*self.__length**2

  def get_circum(self):
    return 3.14*2*self.__length


# 클래스 선언
c1 = Circle(int(input("반지름 >>")))
print("넓이 :", c1.get_area())
print("둘레 :", c1.get_circum() )

c2 = Circle(int(input("반지름 >>")))
print("넓이 :", c2.get_area())
print("둘레 :", c2.get_circum() )


