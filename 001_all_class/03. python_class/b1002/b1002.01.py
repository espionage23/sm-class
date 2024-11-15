# input_str = input("글자를 입력하세요.")

# # 문자가 입력되지 않았을때
# if input_str != "": #빈공빅이 아니냐?라고 물을때 쓰는
#   print("글자를 입력해야된다고")
#   print("종료")
# else:
#   print("입력문자 :", input_str)



# #논리 연산자
# # and(논리곱): 둘 다 참이어야 참 or(논리합): 둘 중 하나만 참이어도 참 not(논리부정): 참이면 거짓, 거짓이면 참

#문자열

#문자열숫자
a = "123"
print(type((a)))  #str
print(type(int(a))) #int
print(type(float(a))) #float


b = "12.3"
# print(type(int(b)))  #이렇게 하면 에러남  소수점이 있는 문자열 숫자는 float로 변경해야함.
print(type(float(b)))  #float

#문자열연결연산자
s1 = "안녕"
s2 = "안녕하세요"
print(s1+s2)
print(a+b)  #변수가 문자열이기에 문자로서 합쳐짐

#문자열 *2 #문자열반복연산
print("안녕"*10) #10번 반복
print("--"*30)

#문자열 슬라이싱
str1 = "안녕하세요.반갑습니다."  # 문자열 자체를 리스트 형태로 봄
print(str1[0]) #해당번호를 넣으면 해당되는 문자를 출력
print(str1[6])
print(str1[2:5]) #해당범위출력: [위치:위치한칸뒤]
print(str1[:5]) #[처음:숫자앞까지]
print(str1[2:]) #[위치:끝까지]
print(str1[1:10:2]) #[위치:숫자앞까지:2씩 건너뜀.]
print(str1[1:10:3]) #[위치:숫자앞까지:3씩 건너뜀.]
print(str1[::-1]) #[처음:끝까지:역순으로]


#자바에서는 [] - 배열 : 배열은 범위가 한번 정해지면 수정이 불가
#파이썬에서는 [] - 리스트 : 범위상관없음.

c = 12.3
print(type(int(c))) #실수는 int타입으로 변경이 가능함.
print(int(c))  #소수점을 버림.
