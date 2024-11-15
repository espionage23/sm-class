# try, except: 프로그램 예외를 처리한느 명령어. 강제종료 예방
# while True:
#   score = 100
#   print("[ 나눗셈 프로그램]")
#   nstr = input("숫자만 입력가능 >>")

#   # 숫자가 아닌것을 입력시 에러, 0을 입력하면 에러
#   try:
#     # print("숫자로 변환이 가능합니다.")
#     num = int(nstr)
#     print("입력된 숫자로 100을 나눔 :",score/num)
#   except:
#     print("숫자로 변환이 안됨.")

try:
  print("입력된 숫자 :",int(print("숫자를 입력하세요. > ")))
except:
  pass