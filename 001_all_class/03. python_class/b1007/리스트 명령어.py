# a,b,c,d,e,f,g = 0,0,0,0,0,0,0
# total = 0

# #a,b,c,d,e의 변수에 숫자를 입력받아 합계를 출력하시오.
# a = int(input("숫자1"))
# b = int(input("숫자2"))
# c = int(input("숫자3"))
# d = int(input("숫자4"))
# e = int(input("숫자5"))
# f = int(input("숫자6"))
# g = int(input("숫자7"))
# total = a+b+c+d+e+f+g
# print("합계:",total)


# a_list = []
# total = 0

# for i in range(10):
#   j = int(input(f"{i+1}번째 숫자를 입력"))
#   a_list.append(j)
#   total += j

# for idx,a in enumerate(a_list):
#   a = int(input(f"{idx+1}번째 숫자"))
#   total += a

# print("합계 : ",total)



# a_list = []
# #1-100 들어가 있는 리스트를 출력하시오.
# for i in range(1,100+1):
#   a_list.append(i)

# print(a_list)

#문자열, 숫자 정수, 실수, 논리형
# a_list = [1,2,3,0,"안녕",True,False]
# print(a_list[0])
# print(a_list[3])
# print(a_list[-1])

#순차적으로 출력
# a_list = [1,2,3,4,5]
# for i in a_list:
#   print(i)

# #역순으로 출력하는 법
# for i in range(1,len(a_list)+1):
#   print(a_list[-(i+1)])
# for i in range(len(a_list)):
#   print(a_list[-(i+1)])

# a_list = [1,2,3,4,5]
# b_list = a_list[::-1]
# print(a_list)
# print(b_list)

# a_list = [1,2,3,4,5]
# # b_list = a_list #얕은 복사   a의 값을 변경하면 b값이 변경
# # a_list[0] = 100
# # print(a_list)
# # print(b_list)

# b_list = a_list[:] #깊은 복사   a의 값을 변경해도 b 값이 변경 안됨
# a_list[0] = 100
# print(a_list)
# print(b_list)


#리스트 출력방법
# a_list = [1,2,3,4,5]
# b_list = [50,100]
# print(a_list[0:3]) #1,2,3
# print(a_list[2:4]) #3,4
# print(a_list[:3]) #1,2,3
# print(a_list[3:]) #4,5
# print(a_list+b_list)
# print(b_list*3)
# print(a_list[::2])# 1,3,5
# print(a_list[::-2])# 5,3,1

#리스트 수정방법
# a_list=[1,2,3,4,5,6,7]
# a_list[3] = 50
# a_list[1:2] = [20,30] #2개 변경시
# print(a_list)

#리스트 삭제
# a_list = [1,2,3,4,5]
# del(a_list) # a_list 자체를 삭제함
# a_list = none #전체 삭제
# a_list = []#전체 삭제
# a_list[1:3] = [] #2개 삭제시 - [2,5]
# print(a_list)

# del 명령어
# del a_list[0] #[2,3,4,5]
# print(a_list)


#리스트 함수
a_list = [1,2,3,4,5,60,3,70,3]
#리스트 함수 추가
# a_list.append(200) # 맨뒤에 추가
# a_list.insert(0,100) #0번째에 100을 삽입   index위치에 해당값 저장

#리스트 함수 삭제
# a_list.pop(2)           # 해당 index의 위치 삭제
# a_list.remove(5)        #리스트 값을 찾아 삭제
# a_list.claer()          #전체삭제
# del(a_list[3])          #해당위치 리스트 삭제
# print(len(a_list))      #리스트 개수
# print(a_list.count(3))  #입력된 값의 존재 개수를 확인
print(a_list)
