import oracledb
import random
import requests
from bs4 import BeautifulSoup
# email 발송관련
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication



def connects():
  user = "ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try:
    conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e:
    print("예외 발생 : ",e)
  return conn

def random_num():
  a = random.randrange(0,10000)
  ran_num = f"{a:04}"
  print(ran_num)
  return ran_num

while True:
  print("[ 커뮤니티 ]")
  print("1. 로그인")
  print("2. 비밀번호 찾기")
  print("3. 회원가입")
  print("0. 프로그램 종료")
  print("-"*30)
  choice = input("원하는 번호 >> ")

  if choice == "1":
    print("[ 로그인 ]")
    user_id = input("아이디 >> ")
    user_pw = input("비밀번호 >>")

    # 오라클 db에 접속해서 member 테이블에서 접속해서 가져옴
    # db 접속
    conn = connects()
    cursor = conn.cursor()
    sql = "select * from member where id=:id and pw=:pw"
    cursor.execute(sql,id=user_id,pw=user_pw)
    row = cursor.fetchone()
    print(row)
    if row != None:
      print(f"로그인 성공 {row[2]}님 환영합니다.")
    else:
      print("아이디 또는 패스워드가 일치하지 않습니다.")
    cursor.close()

    # 평소 했던 방식
    # if user_id == 'aaa' and user_pw =="1111":
    #   print('로그인 성공')
    # else: 
    #   print("로그인 실패")
    #   continue

    print("[ 프로그램에 접속합니다. ]")
    ### 프로그램 구현 ###

  elif choice == "2":
    print("[ 비밀번호 찾기 ]")
    search = input("해당 아이디를 입력하세요. >>")
    # 아이디 존재 확인
    conn = connects()
    cursor = conn.cursor()
    sql = "select * from member where id=:id"
    cursor.execute(sql,id=search)
    row = cursor.fetchone()
    print(row)
    if row != None:
      print("아이디가 존재합니다. 임시 패스워드를 발급합니다.")
      #임시 패스워드 생성
      # email로 보냅니다.
      # 임시번호로 로그인을 했을 경우 로그인 성공이 나타나도록 하시오.
      # 임시번호로 로그인을 했을 경우 로그인 성공이 나타나도록 하시오.

      # 임시 비밀번호
      print(f"임시 비밀번호를 귀하의 email로 발송하였습니다.")

      # email 발송
      smtpName = "smtp.naver.com"
      smtpPort = 587

      # id,pw, 받는 사람 이메일 주소
      sendEmail = "zalstmd23@naver.com"
      pw = "U7LKPCQQNE2E" #깃에 노출됨
      recvEmail = "zalstmd23@naver.com"

      title = "제목: 임시비밀번호 발급 안내"
      content = f"""\
      귀하의 임시 비밀번호는 {random_num()} 입니다.
      """

      # 설정
      msg = MIMEText(content)
      msg['Subject'] = title
      msg['From'] = sendEmail
      msg['To'] = recvEmail
      print(msg.as_string)

      # 서버이름, 서버포트
      s = smtplib.SMTP(smtpName,smtpPort)
      s.starttls()
      s.login(sendEmail,pw)
      s.sendmail(sendEmail,recvEmail,msg.as_string())
      s.quit()

      # 메일발송 완료
      print("메일발송 완료.")

      #

    else:
      print("아이디가 존재하지 않습니다.")
    cursor.close()

  elif choice == "3":
    pass
  elif choice == "0":
    print("프로그램 종료")
    break

