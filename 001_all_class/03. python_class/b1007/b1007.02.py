numbers = [273,103,5,32,65,9,78,800,99]
# 100 이상의 값만 출력하시오.
# for n in numbers:
#   if n >= 100:
#     print(n)

# numbers.sort() #순차정렬 - 낮은 수부터 출력
numbers.sort(reverse=True) #역순 정렬 -높은 수부터 출력

#순서를 거꾸로 출력
print(numbers)
numbers.reverse() #순서를 역순으로 출력
print(numbers)
