import datetime

nowYear = datetime.datetime.now().year

# in_year = input("생년월일 >> 20020312")
in_year = "20020312"

print(in_year)

print(f"현재 나이 : {nowYear-int(in_year[:4])}")