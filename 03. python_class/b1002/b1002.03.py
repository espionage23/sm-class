# #입력한 숫자가 짝수읹, 홀수인지 출력하시오.

# num = int(input("숫자를 입력하시오."))
# if num%2 == 0:
#   print("짝수임")
# else:
#   print("홀수임")


#if - else
#if elif else

#입력한 숫자가 1(포함)보다 크고 10(10포함)보다 작을떄만 정답, 오답

# num = int(input("숫자를 입력하시오."))
# if num <= 1 and num >= 10:
#     print("정답")
# else:
#   print("오답")

# num = int(input("숫자를 입력하시오."))
# if 1<= num <=10:
#     print("정답")
# else:
#   print("오답")

#입력한 숫자가 10(포함)보다 작거나 100(포함)보다 클때 정답입니다.
# num = int(input("숫자를 입력"))
# if num <= 10 or num >=100:
#   print("정답")
# else:
#   print("오답")


# 3,4,5 봄 6,7,8 여름 9,10,11 가을 12,1,2 겨울
# num = int(input("월 입력"))
# if num == 3 or num == 4 or num == 5:
#   print("봄")
# elif num == 6 or num == 7 or num == 8:
#   print("여름")
# elif num == 9 or num == 10 or num == 11:
#   print("가을")
# elif num == 12 or num == 1 or num == 2:
#   print("겨울")
# else:
#   print("숫자를 잘못 입력함")



# 100,99,98 a+ 97,96,95 a 93,92,91,90 a- 89,88 b+ 87,86,84 b 83-80 b- 70점대 c f까지 60점 이하

num = int(input("점수를 넣어라"))
score = ""

if 90 <= num:
  score = "A"
  if 98 <= num:
    score += "+"


if 98 <= num <=100:
  print("A+")
elif 95  <= num:
  print("A")
elif 90  <= num:
  print("A-")
elif 88  <= num:
  print("B+")
elif 84  <= num:
  print("B")
elif 80  <= num:
  print("B-")
elif 70  <= num:
  print("C")
else:
  print("F")
