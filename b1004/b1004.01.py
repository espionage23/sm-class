students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
  [4,'강감찬',100,90,99],
  [5,'김구',90,90,99]
]

# 합계,평균을 추가해서 전체를 출력하시오.
#1 홍길동 100 90 99 289 92.00 이런식으로

for a in students:
  a.append(a[2]+a[3]+a[4])
  a.append((a[2]+a[3]+a[4])/3)

print("학번\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*55)
for a in students:
  print(f"{a[0]}\t{a[1]}\t{a[2]}\t{a[3]}\t{a[4]}\t{a[5]}\t{a[6]:.2f}")

