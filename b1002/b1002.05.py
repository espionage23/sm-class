#문자열 슬리이싱
# str = "좋은 하루되세요. 많은 행복 받으세요. 많은 감사! 많은 돈"
# print(len(str)) # 글자의 길이 수를 확인

# #뒤쪽에서 5자리 전까지 출력
# print(str[:-5])
# print(str[-1]) # -를 붙이면 뒤쪽에서 출력됨
# print(str[::-1])

# list 추가 - append(뒤에 추가), insert(원하는 위치에 추가)
# 삭제 del-위치삭제, remove-값으로 검색해서 삭제
# a_list = [1,2,3]
# #10추가
# a_list.append(10) #index 마지막에 10 추가
# print(a_list)

# a_list.insert(2,100) #index 2번에 100추가
# print(a_list)

# del a_list[1] #index 1번 삭제
# print(a_list)

# a_list.remove(100) #100이라는 값으로 삭제
# print(a_list)

students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99]
]

# print(students[0][3])
# print(len(students))
#반목문
for i in range(10): #시작이 0부터 시작함
  print(i)

for i in range(2,5): #시작:2부터 5이전까지 반복
  print(i)

for i in range(1,10,2):  #시작1부터 10이전까지 step2해서 출력
  print(i)

aArr = [1,2,5,7,8] #list의 값과 index번호를 함게 출력
for i in aArr:  
  print(i)

for i,data in enumerate(aArr):
  print(i,":",data)

aStr = "안녕하세요" #문자열의 값을 1개씩 가져와서 출력
for i in aStr:
  print(i)

# enumerate index번호를 추가해서 가져올수 있음.
for idx in enumerate(aStr):
  print(idx, ":",data)



#번호, 이름, 국어, 영어, 수학
# s = [4,'강감찬',100,100,99]
#s 리스트에 합계 평균을 추가하시오.
# print(s[2])

#합계 점수를 추가해서 추력하시오.
# s.append(s[2]+s[2]+s[2])
# s.append((s[2]+s[2]+s[2])/3)
# students.append(s)