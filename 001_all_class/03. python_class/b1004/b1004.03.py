#0부터 1씩 증가하면서, 10번 실행
for i in range(10):
  print(i)
print("-"*50)
#5부터 10 이전까지 5번 실행 5,6,7,8,9
for j in range(5,10):
  print(j)

print("-"*50)
a_list = [1,2,3,4,5]
for k in a_list:
  print(k)

print("-"*50)
# 파이썬 - 문자열-str, 정수형-int, 실수형-float, 논리형-bool
# 리스트 타입 - []
b_list = [3,5,9,10,20,3,3,10,5,20]
for m in b_list:
  print(m)
# 딕셔너리타입 - {}: json타입과 모양이 같음.  키,값(key,value)
dic = {
  "번호":1,
  "이름":"홍길동",
  "국어": 100,
  "영어": 100,
  "수학": 99,
}
print(dic["번호"])
print(dic["이름"])

for n in dic:  #dic에서 key값을 n에 넣어줌.
  print(n)   #key 값 출력
  print(dic[n])  # key 값의 value 값이 출력이 됨

print("-"*50)
# list 길이: len()
print(len(b_list))

#리스트 안에 해당되는 숫자가 몇개인지 확인 - count
print(b_list.count(3))

# 리스트 추가 - append,insert,extend([2,3])
# 리스트 삭제 - del,remove,clear:모두 삭제