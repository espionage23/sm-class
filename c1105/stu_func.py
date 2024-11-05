import oracledb

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']

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

# 메인화면 출력함수
def main_print():
  print(" [학생성적 프로그램 ]")
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적검색")
  print("4. 학생성적정렬")  # 이름순차, 이름역순, 합계순차, 합계역순
  print("5. 등수처리")
  print("0. 프로그램 종료")
  choice = input("원하는 번호를 입력 >> ")
  return choice


# 학생성적입력
def stu_insert():
  conn = connects()
  cursor = conn.cursor()
  print("[ 학생성적입력 ]")
  name = input("이름 >> ")
  kor = int(input("국어 >> "))
  eng = int(input("영어 >> "))
  math = int(input("수학 >> "))
  total = kor+eng+math
  avg = total/3
  # list
  s_list = [name,kor,eng,math,total,avg]

  # insert, update, delete 경우 conn.commit() 해야 반영됨.
  sql = "insert into students values\
        (students_seq.nextval,:1,:2,:3,:4,:5,:6,0,sysdate)"
  cursor.execute(sql,s_list)
  conn.commit()
  conn.close()
  print("학생성적이 저장되었습니다.")
  print()


# 학생성적 출력함수
def stu_output():
  print("[ 학생성적 입력 ]")
  for s in s_title:
    print(s,end='\t')
  print()
  print("-"*80)
  conn = connects()
  cursor=conn.cursor()
  sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students"
  cursor.execute(sql)
  rows = cursor.fetchall()
  print("개수 : ",len(rows))
  if len(rows)<1:
    print("데이터가 없습니다.")
    return
  for row in rows:
    for r in row:
      print(r,end="\t")
    print()
  print()
  print("데이터 출력완료")


# 3. 함수 검색
def stu_search():
  print("[ 학생성적 검색 ]") # a 포함되어 있는 학생을 검색
  print("1. 이름으로 검색")
  print("2. 합계순 검색")
  choice = input("원하는 번호를 입력하세요. >> ")
  if choice == "1":
    search = input("찾고자 하는 이름을 입력하세요. >>")
    search = '%'+search+'%'
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students where name like :search"
    # 출력부분 #
    for s in s_title:
      print(s,end='\t')
    print()
    print("-"*80)

    # db 연결
    conn = connects()
    cursor=conn.cursor()
    cursor.execute(sql,search=search)
    rows = cursor.fetchall()
    print(f"개수 : {len(rows)}")
    if len(rows)<1:
      print("데이터가 없습니다.")
      return
    for row in rows:
      for r in row:
        print(r,end="\t")
      print()
    print()
    print("데이터 출력완료")


# 4. 성적정렬 함수
def stu_array():
  print("[ 학생성적 정렬 ]")
  print("1. 이름순차 정렬")
  print("2. 이름역순 정렬")
  print("3. 합계순차 정렬")
  print("4. 합계역순 정렬")
  choice = input("원하는 번호를 입력하세요. >> ")

  if choice == "1":
    print("이름순차 정렬")
    for s in s_title:
      print(s,end='\t')
    print()
    print("-"*80)
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd')from students order by name"

  elif choice == "2":
    print("이름역순 정렬")
    for s in s_title:
      print(s,end='\t')
    print()
    print("-"*80)
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd')from students order by name desc"


  elif choice == "3":
    print("합계순차 정렬")
    for s in s_title:
      print(s,end='\t')
    print()
    print("-"*80)
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd')from students order by total"

  elif choice == "4":
    print("합계역순 정렬")
    for s in s_title:
      print(s,end='\t')
    print()
    print("-"*80)
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd')from students order by total desc"

  # db 연결
  conn = connects()
  cursor=conn.cursor()
  cursor.execute(sql)
  rows = cursor.fetchall()
  print(f"개수 : {len(rows)}")
  if len(rows)<1:
    print("데이터가 없습니다.")
    return
  for row in rows:
    for r in row:
      print(r,end="\t")
    print()
  print()
  print("데이터 출력완료")


# 5. 등수정렬
def stu_rank():
  print("[ 등수처리 ]")
  sql = "update students a set rank = (select ranks from (select no,rank() over(order by avg desc) ranks from students)b where a.no = b.no)"
  # db 연결
  conn = connects()
  cursor=conn.cursor()
  cursor.execute(sql)
  rows = cursor.fetchall()
  if len(rows)<1:
    print("데이터가 없습니다.")
    return
  for row in rows:
    for r in row:
      print(r,end="\t")
    print()
  print()
  print("데이터 출력완료")