# num1 = int(input("숫자를 입력하세요.>>"))
# num2 = int(input("숫자를 입력하세요.>>"))

# num1 = 10
# num2 = 5

# print(f"두수 더하기 : {num1+num2}")
# print(f"두수 빼기 : {num1-num2}")
# print(f"두수 곱하기 : {num1*num2}")
# print(f"두수 나누기 : {num1/num2}")


#for문을 활용한 계산
# num1 = [10,20,30]
# num2 = [5,7,3]

# for i in range(len(num1)):
#   print("더하기 :",num1[i]+num2[i])
#   print("뺌 :",num1[i]-num2[i])
#   print("곱하기 :",num1[i]*num2[i])
#   print("나누기 :",num1[i]/num2[i])

#함수사용
# def calc(num1,num2):
#   print("더하기 :",num1+num2)
#   print("뺌 :",num1-num2)
#   print("곱하기 :",num1*num2)
#   print("나누기 :",num1/num2)

# num1 = [10,20,30]
# num2 = [5,7,3]

# for i in range(len(num1)):
#   calc(num1[i],num2[i])

#문자열을 숫자로 변경해서 ,num1,num2로 지정
# numStr = input("숫자 (00,00)>>") #12,5
# num = numStr.split(",")
# num1 = int(num[0])
# num2 = int(num[1])
# calc(num1,num2)


# def calc(num1,num2,num3):
#   print("더하기 :",num1+num2+num3)
#   print("뺌 :",num1-num2-num3)
#   print("곱하기 :",num1*num2*num3)
#   print("나누기 :",num1/num2/num3)

# #3개의 숫자를 입력받아 숫자를 계산하시오. 12,5,3
# numStr = input("숫자 3개 입력 (00,00,00)")
# num = numStr.split(",")
# num1 = int(num[0])
# num2 = int(num[1])
# num3 = int(num[2])
# calc(num1,num2,num3)

# def calc(numStr2):  #배열
#   s1 = 0
#   s2 = 0
#   s3 = 1
#   s4 = 1
#   for i in range(len(numStr2)):
#     s1 += numStr2[i]
#     s2 -= numStr2[i]
#     s3 *= numStr2[i]
#     s4 /= numStr2[i]
#   print("두수 더하기 : ",s1)
#   print("두수 빼기기 : ",s2)
#   print("두수 곱하기 : ",s3)
#   print("두수 나누기 : ",s4)

# numStr = input("숫자 3개 입력 (00,00,00)")
# numStr2 = numStr.split(",")
# numStr2 = [int(i) for i in numStr2]

# calc(numStr2)

# def calc(*n): #가변매개변수
#   print(n)
#   print(len(n))

# calc(1,2,3)

#기본 매개변수 - 매개변수의 개수가 동일
#def calc(n1,n2):
#  print(<n1,n2)
#calc(1,2)

#키워드 매개변수
# def calc(n1 = 50, n2 = 20):
#   print(n1)
#   print(n2)
# calc() #매개변수가 없으면 기본값으로 출력 됨.
# calc(20) #n1에는 20이 n2는 기존값
# calc(300) #키가 없으면 무조건 1번째로 전달이 됨.
# calc(n2=100) #키가 있으면 키겂으로 전달됨.

# print(1,2,3,sep=":",end="\t") #가변매개변수
# print("안녕")

# #함수 내에 선언된 변수는 외부에서 사용할수 없음.
# def calc(v1,v2):
#   global sum  #전역변수   외부에 있는 변수값을 가져옴
#   # sum = 0  #지역변수
#   for i in range(v1,v2+1):
#     sum += i
#   return sum


# sum = 100  #외부의 변수를 사용해서 계산을 하고 싶을 경우
# sum = calc(1,10)
# print(sum)


# def calc(n1,n2):
#   s1 = n1+n2
#   s2 = n1-n2
#   s3 = n1*n2
#   s4 = n1/n2
#   s5 = [s1,s2,s3,s4]
#   return s5

# s5 = calc(10,5) 
# print(s5)




# kim = [] #얕은 복사
# kim = hong
# kim[0] = 100
# print(hong)

# def add(h):
#   for i in range(len(h)):
#     h[i] = h[i]+100

#매개변수가 일반변수일 경우 return 하지 않으면 변수값이 변동이 없음.
# hh = 100
# def add(hh):
#   hh = hh +100

# add(hh)
# print(hh)

#--------------------------------------

#복합변수 - 리스트, 딕셔너리
# hong = [1,2,3,4,5]

# #매개변수가 복합변수일 경우, return 없어도 값이 변경되어 전달 됨.
# def add(h):
#   for i in range(len(h)):
#     h[i] = h[i]+100

# add(hong)
# print(hong)

#전역변수인 경우 함수내에서도 사용이 가능하고 함수 외부에서도 사용이 가능함.
#지역변수는 return 없이는 값이 함수밖으로 나오지 못함.
def calc():
  global sum #전역변수인 경우, 함수에서 변경시 외부에서도 같이 변경이 됨.
  sum = 200

sum = 10 
calc() #함수에서 sum을 200으로 변경이 됨
print(sum) #결과값은 sum이 200이됨