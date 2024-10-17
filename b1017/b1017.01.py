


# a = 10  
# #선언
# def func(a):
#   print("함수내 a:",a)
#   a += 50  
#   return a
#   # global a #전역변수를 가져옴 | 같은 곳을 바라보게 함.
#   # a = 50  #지역변수 - 함수를 종료하면 모두 제거됨.

# #호출   #호출은 함수선언 보다 무조건 밑에 있어야 발동한다.
# a = func(a)   # 리턴시 재선언? 뭔지 모르지만 이 형식을 안하면 값을 받을수 없음
# print("함수 밖: ",a)


# a = 10
# b = 20
# c = 30
# # sum = 0

# # def add(a,b):
# #   return a+b

# # sum = add(a,b)
# # print("a+b의 합계: ",sum)

# #a에 함수를 사용해서, a+b+c의 합을 a에 입력해서 출력하시오.

# sum = 0
# def add(a,b,c,):
#   return a+b+c

# a = add(a,b,c)
# print("a+b+c의 합 : ",a)

subject = ["국어","영어"]
score = []

while True:
  print("1.과목추가")
  print("0.종료")
  choice = input("원하는 번호 >>")
  if choice == "1":
    s_input = input("과목을 추가하세요. >>")
    subject.append(s_input)
  elif choice == "0":
    print("종료")
    break

for i in range(len(subject)):
  score.append(int(input(f"{subject[i]}점수를 입력하세요. >>")))

# num1 = int(input("국어점수 >>"))
# num2 = int(input("영어점수 >>"))
# num3 = int(input("수학점수 >>"))
# num4 = int(input("과학학점수 >>"))
# num5 = int(input("역사학점수 >>"))
sum = 0
for i in range(len(subject)):
  print(f"{subject[i]}:",score[i])
  sum += score[i]
print("합계:",sum)

# print("합계: ",num1+num2+num3+num4+num5)


while True:
  print("[ 과목 생성 프로그램]")
  s_input = input("원하는 과목을 입력하세요.")
  subject.append(s_input)




