import oracledb

# oracle 연결 - sql developer
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")

# 연결확인
# print(conn.version)

# sql 실행창 오픈
# 1개 검색된 데이터 호출
# cursor = conn.cursor()
# sql = "select count(*) from member"
# cursor.execute(sql)

# count1 = cursor.fetchone()
# print("개수 : ",count1)

# 여러 검색된 데이터 내용 호출
cursor = conn.cursor()
sql = "select * from member"
cursor.execute(sql)
rows = cursor.fetchall()

# for row in rows:
#   print(row)

print(rows)
# print(rows[0][0],rows[0][1],rows[0][2])

# 상단
title = ['id','pw','name','email','phone','gender','hobby','mdate']

for i in title:
  print(i,end='\t')
print()
print("-"*150)

conn.close()






