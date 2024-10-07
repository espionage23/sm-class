import random

a_list = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
while True:
  print("       [i,j 좌표]")
  print("\t0\t1\t2")
  print("-"*20)
  for i in range(3):
    print(i,"|",end="\t")
    for j in range(3):
      print(a_list[i][j],end="\t")
    print()

  code = input("좌표를 입력 (0.0) >>")
  codeArr = code.split(".")
  print(f"{code}의 좌표값 :",a_list[codeArr[0]][codeArr[1]])