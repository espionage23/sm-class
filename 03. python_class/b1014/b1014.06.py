import random
# tName = ["이름", "국어", "영어", "수학", "합계",]
fruit = {"바나나":"banana","오렌지":"orange","체리":"cherry", "파인애플":"pineapple","코코넛":"coconut"}
# fName = ["바나나", "오렌지", "체리", "파인애플", "코코넛"] #아래와 같다.
fName = (list(fruit.keys()))


#바나나를 입력하면 영어로 banana
# print(fruit["바나나"])
# print(fruit["오렌지"])

# while True:
#   search = input("과일 이름을입력하세요. >>")
#   if search in fruit:
#     print("영문으로 :",fruit[search])
#   else :
#     print("찾는 단어가 없습니다.")


# print("영단 맞추기. >>")
# for key in fruit.keys():
#   search = input(f"{key}의 영문을 입력하세요.")
#   if fruit[key] == search:
#     print("정답입니다.",fruit[key],search)
#   else:
#     print("오답입니다.")



# print("영단 맞추기. >>")
# search = input("바나나의 영문을 입력하세요.")
# if fruit['바나나'] == search:
#   print("정답입니다.",fruit['바나나'],search)
# else:
#   print("오답입니다.")

#random.shuffle(tName)   #원본이 변경됨
# fName 랜덤순서로 영문퀴즈 시작
re_fname = random.sample(fName,5)
for i in re_fname:
  search = input(f"{i}의 영문을 입력하세요.")
  if fruit[i] == search:
    print("정답입니다.",fruit[i],search)
  else:
    print("오답입니다.",fruit[i],search)