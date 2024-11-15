# a = "안녕하세요."
# print(a[2:-1])


# lists = [1,2,3,4,5]
# print(lists[1:-1])

# a = ""
# print(int(a))
# print("완료")


# 정렬
n_lists = [
  ["존",100,4.5,1000],
  ["박",70,4.2,200],
  ["이",80,4.5,800],
  ["트럼프",90,4.5,10]
]

print("기본 : ",n_lists)
# n_lists에서 1개(n_list)를 x에 대입시켜줌
n_lists.sort(key=lambda x:x[0],reverse=True)
print("금액정렬",n_lists)