# #enumerate() 함수
# a_list = ['홍길동','유관순','이순신','강감찬','김구','김유신','홍길자']

# #for문으로 출력
# for a in a_list:
#   print(a)

# #enumerate() 함수 - index 번호를 출력
# for i,a in enumerate(a_list):
#   print(f"{i+1}:{a}")
# print(a_list)

# a_list = [1,2,3,4,5]
# b_list = [1*1,2*2,3*3,4*4,5*5]

# 리스트 값 변경
# print(a_list)
# a_list[1] = 100
# print(a_list)


# # 리스트 슬라이싱 0부터 4앞까지 (3번까지)
# print(a_list[0:4])

# # 리스트 범위보다 넘어서 출력하면, 에러가 나지는 않지만 범위까지만 출력됨.
# print(a_list[0:10])

# 없는 list위치에 값 수정시 에러
# a_list[5] = 1000
# print(a_list)

# 없는 list위치를 출력시 에러
# print(a_list[10])

# a_list = [1,2,3,4,5]

# print(a_list)
# 리스트의 값을 변경해서 리스트에 저장하는 법
# for idx,a in enumerate(a_list):
#   a_list[idx] = a**2

# 리스트의 값을 변경해서 리스트에 저장하는 법 - 리스트 내포
# a_list = [a**2 for a in a_list]

# print(a_list)

a_list = ["홍길동",'유관순','이순신']
#홍길동님, 유관순님, 이순신님 으로 저장하시오.
a_list = [a+"님" for a in a_list]
print(a_list)