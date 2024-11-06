# employees 테이블에서 이름이 a가 포함되어 있는 이름 출력

import oracledb

# db 연결 함수생성
def connections():
  try:
    conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
    print("db연결 : ",conn.version)
  except Exception as e: print("예외발생 : ",e)
  return conn

# 함수호출
conn = connections()
cursor = conn.cursor()

# 월금 범위를 입력받아 그 사이의 사원을 출력하시오.
num1 = input("숫자1 >>")
num2 = input("숫자2 >>")
sql = "select employee_id,emp_name,salary from employees where salary >= :no1 and salary <= :no2 order by salary"
cursor.execute(sql,no1=num1,no2=num2)


# # 월급이 4000-8000사이의 사원을 모두 출력
# # search = input("검색할 이름을 입력하세요. >> ")
# # search = '%'+search+'%'
# sql = "select employee_id,emp_name,salary from employees where salary between 4000 and 8000"
# cursor.execute(sql)

# # 검색한
# search = input("검색할 이름을 입력하세요. >> ")
# # %를 문자로 인식하기 때문에 밑에와 같이 선언.
# search = '%'+search+'%'
# # emp_name에 a가 포함되어 있는 row를 모두 출력
# sql = "select * from employees where emp_name like :search"
# cursor.execute(sql,search=search)

rows = cursor.fetchall()

title = ['employee_id','emp_name','salary']
a_list = [] #dict 타입으로 변경해서 저장하시오.
for row in rows:
  a_list.append(dict(zip(title,row)))

print(a_list)

cursor.close()