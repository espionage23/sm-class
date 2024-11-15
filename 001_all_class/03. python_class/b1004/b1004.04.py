# # # # # # 1,10까지 for문을 사용해서 출력하시오.

# # # # # for i in range(1,11):
# # # # #   print(i)

# # # # #1,3,5,7,9까지 출력하시오.
# # # # for i in range(10):
# # # #   if i%2 != 0:
# # # #     print(i)

# # # # # 구구단을 출력하시오.
# # # # for i in range(2,9+1):
# # # #   print(f"[{i}단]")
# # # #   for j in range(1,9+1):
# # # #     print(f"{i}X{j}={i*j}")
# # # #   print("-"*20)

# # # #구구단 1,3,5,7,9단만 출력
# # # for i in range(1,9+1):
# # #   if i%2 != 0:
# # #    print(f"[{i}단]")
# # #    for j in range(1,9+1):
# # #      print(f"{i}X{j}={i*j}")
# # #    print("-"*20)

# # # 홀수단 예시2
# # for i in range(1,10,2):  #(시작값,끝값+1,증가값)
# #   for j in range(1,10):
# #     print(f"{i}X{j}={i*j}")

# #for문을 사용해서
# # *
# # **
# # ***
# # ****
# # *****
# for i in range(1,6):
#   print("*"*i) 
# #역순으로 만들어 보셈    
# for i in range(5,0,-1):
#   print("*"*i) 


# for i in [1,2,3]:
#   print("안녕하세요.")

# 1-1번출력, 2-2번출력, 3-3번출력
# for i in [1,2,3]:
#   for j in range(i):
#     print("안녕하세요.")
#   print("-"*30)

# for i in [1,2,3]:
#   print("안녕하세요.\n"*i,end="")
#   print("-"*30)


# 0:안녕하세요.
# 1:안녕하세요.
# 2:안녕하세요.
# for i in range(3):
#   print(f"{i}:안녕하세요.")

# for _ in range(3):
#   print("안녕하세요.")

#1,100까지 숫자의 합
# sum = 0
# for i in range(1,100+1):
#   sum += i
# print("합계 :",sum)

#홀수의 총 합계 100까지
# sum = 0 
# for i in range(1,100+1,2):
#   sum += i
# print("합계 :",sum)


#두수를 입력 받아, 두수까지 합계를 구하시오.
#예시. 3,8 -> 3+4+5+6+7+8
#1. if문 사용
# num1 = int(input("숫자1"))
# num2 = int(input("숫자2"))
# min_num = num1; max_num = num2
# if num1>num2:
#   min_num = num2
#   max_num = num1

# sum = 0
# for i in range(min_num,max_num+1):
#   sum += i
# print("합계 :",sum)

#2.min,max 함수 사용
# num1 = int(input("숫자1"))
# num2 = int(input("숫자2"))

# # min_num = min(num1,num2); max_num = max(num1,num2)

# sum = 0
# for i in range(min(num1,num2),max(num1,num2)+1):
#   sum += i
# print("합계 :",sum)

#3. if문 사용
num1 = int(input("숫자1"))
num2 = int(input("숫자2"))
min_num = num1; max_num = num2
if num1>num2:
  num1,num2 = num2,num1   # 파이썬만 가능 - 두개 변수를 취환
  # num3 = num1
  # num1 = num2
  # num2 = num1

sum = 0
for i in range(num1,num2+1):
  sum += i
print("합계 :",sum)
