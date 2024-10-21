students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99]
]
ss = [4,'강감찬',100,100,99]
# print(students) #한번에 모두 출력

# for s in students: #1개씩 가져와서 출력
#   print(s) #총 3번이 출력되는거임.

#이름이 유관순인것을 출력하시오.
# for s in students:
#   if(s[1]) == '유관순':
#    print(s)

# # ss를 students에 추가
students.append(ss)
# print(students)

# 이순신인 데이터를 삭제하시오.
# for i in students:
#   if(i[1]) == '이순신':
#     students.remove(i)

for idx,i in enumerate(students):
  if i[1] == '이순신':
    del students[idx]

print(students)

#값이 2개 이상 저장이 되면 주소값으로 저장된다.