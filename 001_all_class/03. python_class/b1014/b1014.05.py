#구구단 출력
#2-5단
# for i in range(2,5+1):
#   print("[{}단]".format(i))
#   for j in range(1,10):
#     print("{}*{}={}".format(i,j,i*j))

# #3-9단
# for i in range(3,9+1):
#   print("[{}단]".format(i))
#   for j in range(1,10):
#     print("{}*{}={}".format(i,j,i*j))

# #5-8단
# for i in range(5,8+1):
#   print("[{}단]".format(i))
#   for j in range(1,10):
#     print("{}X{}={}".format(i,j,i*j))


#함수로 구구단
# def gugudan(n2):
#   for i in range(2,n2+1):
#     print("[{}단]".format(i))
#     for j in range(1,10):
#       print("{}X{}={}".format(i,j,i*j))

# # gugudan(2,5)
# # gugudan(3,9)
# # gugudan(5,8)

# nArr = [9,5,7]
# #2-9, 2-5단 2-7단

# for i in nArr:
#   gugudan(i)
#   print("-"*30)

subName = ["국어", "영어", "수학"]
score = {"국어":100, "영어":95, "수학":80}
print(score)
print(score['국어'])
print(subName[0])
print(score[subName[0]])

#예시 1
for i in subName:
  print(i,":",score[i])

#예시 2
# for k,v in score.items():
#   print(k,":",v)