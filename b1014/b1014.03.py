# def num_sum(st,end):   #(매개변수, 매개변수)
#   sum = 0 #지역변수
#   for i in range(st,end+1):
#     sum +=i
#   print("합계 : ",sum)
  
# #전역변수
# sum = 0


# #1-10까지 합계를 출력하시오.
# num_sum(1,10)


# #1-100까지
# num_sum(1,100)


# #2-50까지
# num_sum(2,50)


# #100-1000Rkwl 합계를 출력
# num_sum(100,1000)

#두수를 입력받아, 그 수 사이의 합을 구하시오.
# def num_sum(num1,num2):  #매개변수
#   sum = 0
#   for i in range(num1,num2+1):
#     sum += i
#   print("합계 : ",sum)

# num1 = int(input("숫자1>>"))
# num2 = int(input("숫자2>>")) 

# num_sum(num1,num2)


def num_sum(st,end):
  sum = 0
  for i in range(st,end+1):
    sum += i
  return sum


# num1 = int(input("숫자 >>"))
# num2 = int(input("숫자 >>"))
# print(num_sum(num1,num2))

total = 0
# num_sum(1,10)
# num_sum(1,100)
# total = num_sum(1,10)+num_sum(1,100)
# #1,10  1,100까지의 합의 총합을 출력
# print("합계 : ",total)

#2,50  3,7   5,50까지 사이의 값을 모두 더해서 출력
# print(f"2-50까지의 합 : {num_sum(2,50):,d}")
# print("3-7까지의 합 :",num_sum(3,7))
# print("5-50까지의 합 :",num_sum(5,50))
# total = num_sum(2,50)+num_sum(3,7)+num_sum(5,50)
# print("합계 : ",total)

# def plus(n1,n2):
#   result = n1+n2
#   return result

# #위에와 같은 효과임
# # def plus(n1,n2):
# #   return n1+n2

# print(plus(1,2))
# print(plus(55,45))
# print(plus(50,50))

# 두수를 입력받아 더하기를 출력하시오.
def plus(n1,n2):
  return n1+n2

num1 = int(input("숫자 1 >>"))
num2 = int(input("숫자 2 >>"))
print(plus(num1,num2))

#한줄로 줄이면 이렇게 됨
#print(plus(int(input("숫자 1 >>"),int(input("숫자 2 >>")))))

print("프로그램 종료")