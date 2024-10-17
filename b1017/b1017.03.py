#예외 처리   :  try - except 구문을 사용해서 처리

# try:
#   print("프로그램 시작")
#   # print("프로그램 시작)    # 구문 오류 - 프로그램이 실행전에 오류
#   print(list_a)             # 런타임 오류 - 프로그램 실행중에 오류
# except:
#   print("에러가 발생")

# print("프로그램 종료")
# n_str = input("반지름을 입력 >>")
# try:
# # if n_str.isdigit():
#   num = int(n_str)
#   # 원의 넓이, 둘레
#   print("원 넓이 : ",(num**2)*3.14)
#   print("원 둘레 : ",2*num*3.14)
# except Exception as e:  
# # else:
#   print("정수가 아닙니다.",e)

# list_a = [1,2,3,4,5,"홍길동",5,6,7]
# list_b = []
# #숫자에 *2를 하는 프로그램을 구현하시오.
# try:
#   for a in list_a:
#     list_b.append(a**2)
# except Exception as e:
#   print("에러",e)


# print(list_b)

# print("1")
# try:    #try 구문에 에러가 발생해야 except를 실행시킴
#   print("2")
#   print(3/0)
#   print("3")
#   print("4")
# except:
#   print("5")
#   print("6")

# print("7")
# print("8")

# try - except
# try에 에러가 발생하면 except 실행
# try - except -else
# else는 try 구문에 에러가 없으면 실행

# try - except -finally
#try 실행여부 상관없이 무조건 실행됨.


# print("1")
# try:    #try 구문에 에러가 발생해야 except를 실행시킴
#   print("2")
#   print(3/0)  #에러 발생
#   print("3")
#   print("4")
# except:
#   print("5")
#   print("6")
# else:
#   print("프로그램 에러가 발생하지 않으면 실행")
# finally:
#   print("finally 실행")

# print("7")
# print("8")

# print("파일 open")
# try:
#   print("글쓰기 1")
#   print("글쓰기 2")
#   print("글쓰기 3")
#   print("str -> 딕셔너리 입력 4")  #에러
#   print("글쓰기 5")
#   print("글쓰기 6")
# except:
#   print("잘못된 타입이 들더왓습니다.")
# finally:
#   print("파일 close")

# print("프로그램을 종료합니다.")

# try:
#   f = open('b1017/a.txt','w',encoding='utf-8')
#   f.write("안녕하세요.1\n")
#   f.write({"a":1})
#   f.write("안녕하세요.2\n")
# except Exception as e:
#   print("에러 ",e)
# finally:
#   f.close()

numbers = [52,273,32,103,90,10,275,1,2,1,2,12]
# a = "12351200"
# b = a.find(1)
# print(b)
try:
  print(numbers.index(52))
  print(numbers.index(1))
  print(numbers.index(3))
  print(numbers.index(32))
  print(numbers.index(90))
except Exception as e:
  print("찾는 번호가 없습니다.",e)


  

