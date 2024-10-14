import random

random_num = random.randint(1,100)
count = 0

for i in range(10):
    in_num = int(input("숫자를 입력하라"))
    if random_num < in_num:
        print("숫자가 큽니다.")
    elif random_num > in_num:
        print("숫자가 작습니다.")
    else:
        count = 1
        print("정답입니다.")
        break

if count == 0:
    print("실패 정답:",random_num)