import oracledb

def connect():
  user="ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try:
    conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외처리",e)
  return conn



### 입력한 달 이상의 입사한 사원을 출력하시오.
d_day = int(input("숫자를 입력 >> "))
# if len(d_day) == 1:
#   d_day = "0"+d_day

conn = connect()
cursor = conn.cursor()
sql = "select emp_name,hire_date from employees where substr(hire_date,4,2) >= :d_day"
cursor.execute(sql,d_day=d_day)
rows = cursor.fetchall()
if rows == None:
  print("에러")
else:
  for row in rows:
    print(row)



