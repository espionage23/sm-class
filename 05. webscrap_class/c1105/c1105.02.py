
# 2. 함수선언 가변매개변수
def func(*num):
  print(num)
  print(len(num))

# 함수 호출
func(10)
func(10,20)
func(10,20,30)



# # 1. 함수 선언 - 기본매개변수를 사용
# def func(num1,num2):
#   print(num1)
#   print(num2)

# # 함수호출
# func(10,20)

# 함수의 매개변수 개수를 정확히 맞춰야 에러가 나지 않는다.
# func(10,20,30) #에러
# func(10) #에러