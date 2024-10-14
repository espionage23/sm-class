def operate(count):
  for i in range(count):
    print("한국어 인사 : 안녕하세요.")

while True:
  print("[외국어 인사]")
  print("1. 영어 인사")
  print("2. 일본어 인사")
  print("3. 중국어 인사")
  print("4. 프랑스어 인사")
  choice = input("원하는 번호를 입력하세요 >>")
  count = int(input("한국어 반복횟수를 입력하세요 >>"))
  
  if choice == "1":
    operate(count)
    print("영어 인사 : Hello")
  elif choice == "2":
    operate()
    print("일본어 인사 : こんにちは Kon'nichiwa")
  elif choice == "3":
    operate()
    print("중국어 인사 : 你好 Nǐ hǎo")
  elif choice == "4":
    operate()
    print("프랑스어 인사 : Bonjour")