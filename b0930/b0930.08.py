# #list 추가방법   추가방법은:append: 제일 뒤에 추가, insert: 원하는 위치에 추가
# a_list = [1,2,3]
# print(a_list)
# a_list.append(4)  
# print(a_list)
# a_list.append(10)
# print(a_list)
# a_list.insert(0,50)     #insert. (0,50) 앞에는 원하는 위치 뒤에는 값
# print(a_list)
# a_list.insert(3,20)
# print(a_list)

# #삭제 del:index위치에 있는 데이터 삭제, remove,:데이터 값으로 삭제
# del a_list[0]
# print(a_list)
# del a_list[2]
# print(a_list)

# a_list.remove(4)  #위치에 있는 값이 아니라 숫자 4가 사라짐
# print(a_list)

stu = [1,'홍길동',100,100,100,99]
## 합계, 평균을 추가해서 넣으셈

stu.append(stu[2]+stu[3]+stu[4]+stu[5])
stu.append((stu[2]+stu[3]+stu[4]+stu[5])/4)
print(stu)
