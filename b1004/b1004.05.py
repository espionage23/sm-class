# # #구구단 입력한 단까지 출력하시오.3 -> 123 5 ->12345

# # a_input = int(input("숫자를 입력"))
# # for i in range(a_input,a_input+1):
# #   for j in range(1,10):
# #     print(f"{i} X {j} = {i*j}")

# # 000 001...999까지 출력
# #방법 1
# # for i in range(0,10):
# #   for j in range(0,10):
# #     for k in range(0,10):
# #       print(f"{i}{j}{k}")
# #방법 2
# for i in range(000,999+1):
#   print(f"{i:03d}")

#for문을 출력
for k in range(1,10):
  print(f"[{k}단]",end="\t\t")
print()
for i in range(2,10):
  for j in range(1,10):
    print(f"{j} X {i} = {j*i}",end="\t")
  print()