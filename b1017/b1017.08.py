import datetime
import os

# member 딕셔너리 저장
members = []
m_title = ['id','pw','name','nicName','address','money']

# csv 파일 불러오기
f = open('b1017/member.csv','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line : break
  # m 리스트 저장
  m = line.strip().split(",") 
  m[5] = int(m[5])
  # m 리스트에 딕셔너리 저장
  members.append(dict(zip(m_title,m)))
f.close() 


###  cart.txt 파일, members 딕셔너리 저장
cartNo = 0
cart = []
c_keys = ["cno","id","name","pCode","pName","price","date"]


# isfile : 파일인지 확인, isdir: 디렉토리인지 확인, exists : 파일이 존재하는지 확인.
if os.path.isfile("b1017/shop_cart.txt"):
  f = open('cart.txt','r',encoding='utf-8')
  while True:
    line = f.readline()
    if not line: break
    c = line.strip().split(",")
    c[0] = int(c[0])
    c[5] = int(c[5])
    cart.append(dict(zip(c_keys,c)))
  f.close()