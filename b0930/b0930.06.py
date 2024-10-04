#사칙연산  및 추가적 연산
# a = 5; b = 3 #1줄 형태로 표현시 ; 넣어줘야됨.
# #/,%,//,**

# print("{},{},{},{}".format(a/b,a%b,a//b,a**b))

#사칙연산 우선순위
# print(2+2-2*2/2*2)

# 특정숫자 a = 0,1,2,3,4,5
# 1,3,5,7,9
# 2x+1

# x = 1,2,3,4,5,6,7,8,9
# 1
# x = 11,12,13,,,,,20
# 11
# x = 21,,,,,30
# 21

#여러줄을 1줄로
# aa = 10
# bb = 5
# a = 10; b=5 #1줄로 만드는 방법
# s1,s2,s3 = 1,2,3 #1줄 선언 방식


# 문자형숫자 변환
# a = "100"
# b = "10.5"
# c = "안녕"
# print(float(a)) # 정수형 문자열 -> 정수타입, 실수타입 변경가능
# print(int(b)) # 실수형 문자열 -> 실수타입 변경가능
# print(float(c)) # 글자는 숫자형타입으로 변경불가

#숫자를 문자열로 변환    문자열 + 숫자: 불가능
# a = 100
# b = 10
# print(str(a)+str(b))

#복합대입연산자 +=, -=, *=, /=, //=, %=, **=
# a = 10
# a+=5; print(a)
# a-=5; print(a)
# a*=5; print(a)
# a/=5; print(a)
# a//=5; print(a)
# a%=5; print(a)
# a**=5; print(a)

#원의 넓이 : 반지름*반지름 *3.14
# 반지름을 입력받아, 원의 넓이를 구하시오.
# c = int(input("반지름"))
# print("원 넓이: {}".format(c*c*3.14))

# 2개의 길이를 입력받아, 삼각형의 넓이, 직사각형의 넓이를 구하시오.
# num1 = int(input("길이1"))
# num2 = int(input("길이2"))
# print("삼각형:{}, 사각형:{}".format((num1*num2*0.5),(num1*num2)))

# length = input("2개 길이를 입력하세요.")
# print(length.split(" "))
# l_list = length.split(" ")
# print("삼각형의 넓이 :{}".format(float(l_list[0])*float(l_list[1])%0.5))

# stu_data=['홍길동',100,100,100,99]
# #학생 이름: 홍길동 국어:100 영어:100 수학:100 과학:99 합계: 평균:

# name='홍길동'
# kor=100; eng=100; math=100; sine=99; total = kor+eng+math+sine; avg = total/4
# # print("이름:{}, 국어:{}, 영어:{}, 수학:{}, 과학:{}, 합계{}, 평균:{}".format(name,kor,eng,math,sine,total,avg))

# print("이름 :{}".format(stu_data[0]))
# print("국어 :{}".format(stu_data[1]))
# print("영어 :{}".format(stu_data[2]))
# print("수학 :{}".format(stu_data[3]))
# print("과학 :{}".format(stu_data[4]))
# print("합계 :{}".format(stu_data[1]+stu_data[2]+stu_data[3]+stu_data[4]))
# print("평균 :{}".format(stu_data(stu_data[1]+stu_data[2]+stu_data[3]+stu_data[4])/4))



# stu_data=['홍길동',100,100,100,99]

# for s in stu_data:
#   print(s)

stu_title = ['번호','이름','국어','영어','수학','과학','합계','평균']
stu_datas =[
  [1,'유관순',100,100,100,99],
  [2,'이순신',100,99,98,99],
  [3,'김구',80,100,90,99]
]
# #이순신의 평균을 출력하시오.
# print("이순신의 평균 : {}".format((stu_datas[0][1]+stu_datas[0][2]+stu_datas[0][3]+stu_datas[0][4])/4))

# 학생데이터에서 합계, 평균을 추가해서 1줄로 출력하시오.
print("                    [학생성적 프로그램]")
# for s_t in stu_title:
#   print("{}".format(s_t),end='\t')
  # print()
  # print("-"*60)
  # print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(stu_title[0],stu_title[1],stu_title[2],stu_title[3],stu_title[4],stu_title[5],stu_title[6],stu_title[7],))
  # print("-"*60)
  # print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(s_t[]))

for s in stu_datas:
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(s[0],s[1],s[2],s[3],s[4],s[5],s[2]+s[3]+s[4]+s[5],(s[2]+s[3]+s[4]+s[5])/4))