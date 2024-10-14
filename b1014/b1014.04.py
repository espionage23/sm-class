#함수선언
def calc(num1,num2,op):
  result = 0
  if op == "+":
    result = num1 + num2
  elif op == "-":
    result = num1 - num2
  elif op == "*":
    result = num1 * num2
  else:
    result = num1 / num2
  return result

num1= int(input("숫자 1>>"))
num2= int(input("숫자 2>>"))

op = input("+, -, *, / 중 하나를 선택")

print("결과값 : ",calc(num1,num2,op))