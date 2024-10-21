# 25개 1차원 리스트 -> 1,25 입력한 후 랜덤으로 다시 출력하시오.
# [5,5] 리스트


import random

aArr = []
for i in range(25):
  aArr.append(i+1)

random.shuffle(aArr)
# print(aArr)

a_list = []
for i in range(5):
  a= []
  for j in range(5):
    a.append(aArr[5*i+j])
  a_list.append(a)

while True:
  print("\t0\t1\t2\t3\t4")
  print("-"*50)
  for i in range(5):
    print(i,end="\t")
    for j in range(5):
      print(a_list[i][j],end="\t")
    print()  

  #값을 입력하면 해당좌표를 출력하시오.
  re = int(input("값을 입력 >>"))
  if 0>re or re>26:
    print("1에서 25사이의 값을 입력해라")
    continue

  for i in range(5):
    for j in range(5):
      if a_list[i][j] == re:
        print(f"좌표 값:[{i,j}]")
        a_list[i][j] = 0
        break
    
  
    
  # re = input("좌표를 입력하세요.(0.0)>>")
  # result = re.split(".")
  # print("좌표 값 :",a_list[int(result[0])][int(result[1])])

