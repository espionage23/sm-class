#데이터 값이 1개일때#
# num = 10 #num의 메모리 주소값
# num2 = num #num2의 메모리 주소값이 다름.

# num2 = 20 #num2를 변경해도 num의 값은 변경이 안됨.

# print(num)
# print(num2)


#얕은 복사 - 주소값만 복사됨.
a = [1,2,3,4,5]
b = a
b[0] = 100

print(a)

print(b)
