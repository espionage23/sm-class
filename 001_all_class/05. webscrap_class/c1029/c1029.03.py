import oracledb
## sql developer 실행
conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')

## sql 창이 열림
cursor = conn.cursor()

# sql 작성, 실행
num1 = input("숫자를 입력1 >>(,해서 입력하시오.) ")
n_list = num1.split(",")

# num2 = input("숫자를 입력2 >> ")
# num3 = input("숫자를 입력3 >> ")
# n_list = [num1,num2,num3]
# no = 10,20,30을 검색해서 출력하시오.

# 3. excute함수 : 리스트로 값 전달
# execute 뒤에는 dict, list, tuple 타입만 가능
sql = "select * from students where no in(:1,:2,:3)"  
cursor.execute(sql,n_list)

# # 2. excute함수 : 변수를 추가
# sql = "select * from students where no in(:no1,:no2,:no3)"  
# cursor.execute(sql,no1=num1,no2=num2,no3=num3)

# # 1. excute함수 : 변수 key값 전달
# sql = "select * from students where no >=:no"  
# cursor.execute(sql,no=num)

# f 함수로 가져올때
# sql = "select * from students where no >={no}"    # f 함수로도 가져올 수 있음
# cursor.execute(sql)

# 데이터 가져오기 - fetchone() : 1개만, fetchmany() : 숫자만큼만, fetchall() : 전부
rows = cursor.fetchall()
titles = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']
for title in titles:
  print(title,end="\t")
print()
print("-"*80)

for row in rows:
  for i,r in enumerate(row):
    if i == 1:
      print(f"{r:12s}",end='\t')
      continue
    if i == 6:
      print(f"{r:.2f}",end='\t')
      continue
    if i == 8:
      # strftime() 함수 : 날짜포맷 함수 %Y = 2024, %y = 24
      print(r.strftime("%Y-%m-%d"),end='\t')
      # print(f"{r[0]}",end='\t')
      continue
    print(r,end='\t')
  print()


# 종료
conn.close()

