
#10번의 도전에서
# 입력한 숫자가 더 크면 작은수를 입력하셔야 합니다.
# 입력한 숫자가 더 작으면 큰수를 입력하셔야 합니다.
# 10번 도전에서 맞추지 못하면, 10번 도전에 실패했습니다. 랜덤숫자 : 10
#도전에 성공했습니다. 랜덤숫자 : 10

# import random
# r_num=random.randint(1,100)
# count = 0
# for i in range(10):
#   input_num = int(input("숫자를 입력하세요."))
#   if input_num < r_num:
#     print("숫자가 작습니다.")
#   elif input_num > r_num:
#     print("숫자가 큽니다.")
#   else:
#     print("정답 정답번호 : ",r_num)
#     count = 1
#     break

# if count == 0:
#   print("실패 정답번호 : ",r_num)

import random
r_num = random.randint(1,100)
i = 0 #반복하는 변수
count = 0 #확인하는 변수
print(r_num)
while(i<10):
  num = int(input(f"{i+1}번째 숫자를 입력하세요."))
  if r_num < num:
    print("입력한 숫자가 크다")
  elif r_num > num:
    print("숫자가 작더")
  else:
    print(f"정답 랜덤숫자:{r_num}")
    count = 1
    break
  i += 1

if count == 0:
  print(f"10번쨰 도전에 실패함. 랜덤숫자:{r_num}")


