# aArr = [2,3,4,6,7,8,9,10]

# #50,100추가하시오.
# aArr.append(50)
# aArr.append(100)
# print(aArr)

# #2번자리에 30을 추가하시오.
# aArr.insert(2,30)
# print(aArr)

# #숫자 6을 삭제하시오.
# aArr.remove(6)
# print(aArr)

# #index0,3 데이터를 삭제하시오.
# del aArr[0]
# del aArr[3]
# print(aArr)

# all_list = [
#  [1,'홍길동',100],
#  [2,'유관순',200],
#  [3,'이순신',100]
# ]
# a = [3,'이순신',100]

#데이터 값으로 삭제 - remove
# all_list.remove(a)
# print(all_list)

# 이름이 유관순인것을 삭제하시오.
# remove 방식
# for i in all_list:
#   if i[1] == '유관순':
#     all_list.remove(i)
# print(all_list)

#del 방식
# for idx,i in enumerate(all_list):
#   if i[1] == '유관순':
#    del all_list[idx]
# print(all_list)


students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
  [4,'강감찬',100,100,99],
  [5,'김구',90,90,99]
]

#이름을 입력 받아 같은 이름이 있으면 데이터 삭제 없으면 없습니다로 출력하시오.

name = input("이름을 입력하시오.")

for idx,i in enumerate(students):
  if i[1] == name:
    del students[idx]
    print(students)
  else:
    print("이름이 없다")
    break

