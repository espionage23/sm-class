import random
lotto = [0]*6+[1]*3
random. shuffle(lotto)
a_list = [
  [0,1,0],
  [0,0,1],
  [1,0,0]
]
for i in range(3):
  for j in range(3):
    a_list[i][j] = lotto[3*i+j]
    

aa_list = [
  ["로또","로또","로또"],
  ["로또","로또","로또"],
  ["로또","로또","로또"]
]

while True:
  my_money = int(input("얼마 거실? >>"))

  print("     [i,j 좌표]")
  print("\t0\t1\t2")
  print("-"*30)
  for i in range(3):
    print(i,"|",end="\t")
    for j in range(3):
      print(aa_list[i][j],end="\t")
    print()  #\n의 역할

  code = input("좌표를 입력하세요.(0.0)>>")
  codeArr = code.split(".")
  if a_list[int(codeArr[0])][int(codeArr[1])] == 1:
    aa_list[int(codeArr[0])][int(codeArr[1])] == "당첨"
    print(f"{codeArr} 당청금:{my_money*10:,d}")
  else:
    a_list[int(codeArr[0])][int(codeArr[1])] == 0
    aa_list[int(codeArr[0])][int(codeArr[1])] == "꽝"
    print(f"{codeArr} 랄로 : {my_money}")
  printArr = print("좌표값 : ",a_list[int(codeArr[0])][int(codeArr[1])])
  