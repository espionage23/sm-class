# # 2차원 리스트
# a_list = [
#   [1,2,3,4],
#   [5,6,7,8],
#   [9,10,11,12]
# ]

# #2차원 리스트 -> for문을 2번사용한다. (데이터가 다 안들어오기 때문.)
# for i in a_list:
#   for j in i:
#     print(j)

#[3,3] 리스트 [1,2,3],[4,5,6],[7,8,9]
#1-9까지 for문을 사용해서, 2차원 리스트에 추가하시오.
# a_list = []
# for i in range(0,3):
#   a = []
#   for j in range(0,3):
#     y = 3*i+(j+1)
#     a.append(y)
#   a_list.append(a)
# print(a_list)

#예시 2
# a_list = [] #0항, 1항, 2항,...8번항
# for i in range(9):
#   a_list.append(i+1)

# b_list = []
# for i in range(9):
#   b = []
#   if(a_list[i]%4)==0:  #1,2,3,4,5,6,7,8,9
#     b.append(a_list[i])  


# print(b_list)


# #1-9까지 리스트 추가하시오.
# b_list = []
# for i in range(1,10):
#   b_list.append(i)
# print(b_list)


#for문을 2번 작성해서 1,25까지 5,5 리스트 생성하시오.
a_list = []

for i in range(5):
  a = []
  for j in range(5):
    a.append(5*i + (j+1))
  a_list.append(a)

print(a_list)