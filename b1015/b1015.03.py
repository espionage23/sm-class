# 기본 매개 변수로 값 전달 - return이 필요, 값 전달 필요
def plus(a):
  a += 100
  print("지역변수 a :",a) #110 #밖에서 값은 전달 받았지만 보내진 않았음
  return a

#전역변수
a = 10
a = plus(a)  #a변수에 값을 전달해야만 값이 변경이 됨.
print("전역변수 a :",a) #10   #리턴 값을 안받아서 10인거임

#------------------
#복합매개변수로 값 전달 - 리스트, 딕셔너리, return이 필요없다.
def plus(a):
  a[0] = 100
  a[1] = 200
  print("지역변수 a :",a)
  # return a


#전역변수
a = [10,20]
plus(a)
print("전역변수 a :",a) #[100,200]