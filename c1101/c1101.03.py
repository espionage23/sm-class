# 학생성적프로그램
# 1. 학생성적입력
# 2. 학생성적 출력
# 3. 학생성적 검색
# students 테이블을 사용해서
# students_seq 생성
# 번호,김유신,99,98,96,합계,평균,등수,입력일

import oracledb

## db 연결 함수 선언
def connects():
  user="ora_user"
  password="1111"
  dsn="localhost:1521/xe"
  try:
    conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e:
    print("예외처리",e)
  return conn

# 프로그램
while True:
  print(" [학생성적 프로그램 ]")
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적검색")
  choice = input("원하는 번호를 입력 >> ")

  if choice == "1":
    print("[ 학생성적입력 ]")
    name = input("이름 >> ")
    kor = int(input("국어 >> "))
    eng = int(input("영어 >> "))
    math = int(input("수학 >> "))
    total = kor+eng+math
    avg = f"{total/3:.2}"
    rank = 0

    s_list = [name,kor,eng,math,total,avg,rank]
   # db 접속
    conn = connects()
    cursor = conn.cursor()
    sql = "insert into mem(name,kor,eng,math,total,avg,rank)\
            values(:1,:2,:3,:4,:5,:6,:7)"
    cursor.execute(sql,s_list)
    conn.commit()
    cursor.close()
    print("입력이 완료되었습니다.")


  elif choice == "2":
    pass 
  elif choice == "3":
    pass 



#  # db 접속
#   conn = connects()
#   cursor = conn.cursor()
#   sql = "select * from member where id=:id and pw=:pw"
#   cursor.execute(sql,id=user_id,pw=user_pw)
#   row = cursor.fetchone()
#   cursor.close()