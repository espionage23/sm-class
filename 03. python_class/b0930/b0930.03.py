# name = "홍길동"
# num = 100
# num2 = 100
# num3 = 99
# print("%s 합계 : %d" % (name,num+num2+num3))

# #포맷방식
# print("{} 합계 : {}".format(name,num+num2+num3))
# print("%s 평균 : %.2f" % (name,(num+num2+num3)/3))
# print("{} 평균 : {:.2f}".format(name,(num+num2+num3)/3))

# #숫자 : 12.12345 , 456.78940, 2.252525
# #소수점 2자리까지만 출력
# # 숫자 : 12.12 , 456.79, 2.25

# print("숫자 : {2:.2f}, {0:.2f}, {1:.2f}".format(12.12345 , 456.78940, 2.252525)) # :앞에 배치 순서를 넣어서 출력값의 순서를 바꿀수 있음


# print("\*")
# print("안녕\n하세요.")
# print("안녕\t하세요.")
# print("안녕\b하세요.")


# print("""음주운전 사실을 부인하던 김씨는 사고 열흘 만에 범행을 시인했다.\n경찰은 음주운전 혐의도 적용해 김씨를 검찰에 넘겼지만 기소 단계에서는 빠졌다.\n역추산만으로는 음주 수치를 확정하기 어렵다는 것이 검찰 판단이었다.""")

print("{} 평균 : {:.2f}".format("홍길동",(100+100+99)/3))
name = "홍길동"
# f함수 프린트 소수점 처리 : format을 적용후 변수 전달
avg = "{:.2f}".format(99.666667)
print(f"{name} 평균 : {avg}")


#### f함수 소수점 처리
a = 1.12345
print(f"소수점 2자리 출력 :{a:.2f}")

print("출력이 됩니다.")

print("""\
1.음주운전 사실을 부인하던 김씨는 사고 열흘 만에 범행을 시인했다.
경찰은 음주운전 혐의도 적용해 김씨를 검찰에 넘겼지만 기소 단계에서는 빠졌다.
역추산만으로는 음주 수치를 확정하기 어렵다는 것이 검찰 판단이었다.""")


