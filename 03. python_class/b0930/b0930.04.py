# # var1 = 100
# # var2 = var1
# # var3 = var2
# # var4 = var3

# # print(var4)

# # v4 = v3 = v2 = v1 = 10
# # print(v4)

# # name = "홍길동"
# # print(type(name))

# # level = '3레벨'
# # print(type(level))

# # n = 3.14
# # print(type(n))

# # num = 100
# # print(type(num))

# # a_bool = True #True, False는 무조건 대문자로 들어감
# # print(type(a_bool))



# a = '100'
# b = '200'
# name = "홍길동"
# print(type(a))
# print(type(b))
# print(a+b) #문자연결연산자 100200으로 나옴
# print(int(a)+int(b)) #타입을 정수로 변경
# # print(int(name)) # 문자를 숫자로는 변경이 불가능함. 문자로된 숫자만 가능하다.
# c = "3.14"
# print(int(float(c))) #실수로된 문자는 실수형으로 변경후 정수로 변경해야함

# print(str(c)) #실수형을 문자열로 변경

# d = "True"
# print(bool(d)) #문자열로 된 불형을 불형으로 변경

# #타입 변경 - str, float, int, bool



# #name, kor, eng, math,avg 출력
# 홍길동 100,100,99 합계, 평균을 1줄에 출력하시오. 평균은 소수점 2째자리까지만  format,f함수 사용
#input으로 입력을 받아야함

name = input("이름")  
kor = int(input("국어점수"))    #임마들은 다 문자로 들어오기 때문에 숫자로 바꿔줘야함.
eng = int(input("영어점수"))
math = int(input("수학점수"))
total = kor+eng+math
avg = (kor+eng+math)/3

print("이름: {} 국어점수:{}, 영어점수:{}, 수학점수:{}, 합계:{}, 평균:{:.2f}".format(name,kor,eng,math,total,avg))
# print(f"{},")