# i = 0
# while(i<10):
#   print(i)
#   i += 1

# for i in range(10):
#   print(i)


##구구단을 출력하시오.
# i = 1
# while i<10:
#   j=1
#   while j<10:
#     print(f"{i} X {j} = {i*j}")
#     j+=1
#   i+=1

# for i in range(1,10):
#   for j in range(1,10):
#     print(f"{i} X {j} = {i*j}")

# i = 0
# while True: #무한반복
#   print(i); i+=1

#입력한 숫자를 계속 더하는 프로그램을 만드시오.
#0이 입력되면 프로그램을 종료 할 것.

# i = 0
# while True:
#   num = int(input("숫자를 입력"))
#   if num == 0:
#     print("프로그램을 종료합니다.")
#     break
#   i+=num
#   print("합계 :",i)

# break는 반복문을 종료할때 사용, 가장 가까운 반복문의 반목문을 종료함.
# i =0; j=0
# while i<10:
#   print("번호1 :",i)
#   while j<10:
#     if j == 5 :
#       break  # j의 반복문만 브레이크
#     print("번호 :",j)
#     j += i 

# 이중 while문 i=1,10 j=1,10 - j의 출력을 1,3,5,7,9

# i,j = 1,1
# while i<10:
#   while j<10:
#     if j % 2 ==0:
#       j+=1
#       continue
#     print(i,j)
#     j+=1
#   j=1; i+=1

# 두 수를 입력 받아, 더하기, 빼기, 곱하기, 나누기
# while True:
#   num = int(input("숫자1"))
#   num2 = int(input("숫자2"))
#   if num2 == 0:
#     break
#   print("두수의 사칙연산")
#   print("-"*50)
#   print("1. 더하기")
#   print("2. 빼기")
#   print("3. 곱하기")
#   print("4. 나누기")
#   print("-"*50)
#   choice = int(input("원하는 번호를 입력하세요."))
#   if choice == 1:
#     print("결과값 :",num+num2)
#   elif choice == 2:
#   print("결과값 :",num-num2)
#   elif choice == 3:
#   print("결과값 :",num*num2)
#   elif choice == 4:
#   print("결과값 :",num/num2)

s_list = [1]
no = 1
while True:
  #번호, 이름, 국어, 영어, 수학
  print("이름을 입력")
  name = input("이름을 입력(종료 :0)")
  if name == '0':
    break
  kor = int(input("국어점수 입력"))
  eng = int(input("영어점수 입력"))
  math = int(input("수학점수 입력"))
  print(f"번호:{no},국어:{kor},영어:{eng},수학{math}, \합계{kor+eng+math}, 평균 {(kor+eng+math)/3:.2f}")
  no += 1

print("프로그램을 종료")