# 1. readline()   # 얘는 한줄씩 읽어오기
# 가장 바깥 폴더의 위치에서 파일을 찾음
# f = open('a.txt','r',encoding = 'utf8')

# 절대경로를 사용
# f = open('c://aaa/a.txt','r',encoding = 'utf8')
# f = open('b.txt','r',encoding = 'utf8')
# while True:
#   line = f.readline()
#   if not line: break
#   print(line.strip()) #/n 값을 생략
# f.close()

#파일읽기 - r
#위치에 파일이 없으면 에러

# 2. readlines()   # 얘는 모든글을 읽어오기
# f = open('a.txt','r',encoding='utf-8')
# lines = f.readlines()
# for line in lines:
#   print(line.strip())
# print(type(lines))
# f.close()


# 3. read()  #
# f = open('a.txt','r',encoding='utf-8')
# # print(type(f))
# for line in f:
#   print(line.strip())

# f.close()


##### 파일쓰기  - w - #####   파일을 생성후 글자 입력
# f = open('aa.txt','w',encoding='utf-8')
# f. write("안녕하세요.1")
# f. write("안녕하세요.2\n")
# f. write("안녕하세요.3")
# f.close()
# print("글쓰기 종료")

# f = open('aa.txt','w',encoding='utf-8')
# for i in range(1,11):
#   data = f"안녕하세요.{i}\n"
#   f.write(data)
# f.close()
# print("종료")

# while True:
#   print("[ 메모장 ]")
#   data = input("저장하려는 글자를 입력하세요.")
#   f = open('aa.txt','w',encoding='utf-8')
#   f.write(data)
#   f.close()
#   print("종료")

# ###  파일 이어쓰기  - a - ###
# while True:
#   print("[ 메모장 ]")
#   data = input("저장하려는 글자를 입력하세요.")
#   f = open('aa.txt','a',encoding='utf-8')
#   f.write(data+"\n")
#   f.close()
#   print("종료")


###   파일 with    ###   #close()를 하지 않아도 됨.
with open('aa.txt','w',encoding='utf-8') as f:
  f.write("안녕.")









