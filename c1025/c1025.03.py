a = ['1만','3,450','1.7만','500','1,000']

# float 타입으로 변경해서 리스트로 저장.

def chg(val):
  r_val = None
  if '만' in val:
    r_val = float(val[:-1])*10000
  else:
    r_val = float(val.replace(",",""))
  return r_val
  
a_list = list(map(chg,a))

print(a_list)
# 최대값
print(max(a_list))
# 최소값
print(min(a_list))
# 역순정렬
a_list.sort(reverse=True)
print(a_list)