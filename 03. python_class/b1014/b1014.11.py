students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
stuNo = len(students)
#함수호출
def stu_input(stuNo,students):
  while True:
    no = stuNo + 1
    name = input(f"{no}번째 학생 이름을 입력하시오. (0. 이전페이지 이동) >>")
    if name == "0":
      break
    score = []
    for i in range(3):
      t = int(input(f"{s_title[i+2]}점수를 입력하세요."))
      score.append(t)
      total += t

    # kor = int(input("국어 점수를 입력 >>"))
    # eng = int(input("영어 점수를 입력 >>"))
    # math = int(input("수학 점수를 입력 >>"))
    rank = 0
    # students.append({"no":no, "name":name,"kor":score[0], "eng':score[1], "math":score[2], "total":total, "avg":avg:.2f, "rank":rank})
    stuNo += 1
    return stuNo


stu_input(stuNo,students)
print(students)