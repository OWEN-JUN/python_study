#2020년 나이를 기반으로 학년계산

birth = int(input("태어난 년도를 입력하세요 >>"))

age = 2020 - int(birth) + 1

print(age,"세")
if age <= 26 and age >= 20:
    print("대학생")
elif age < 20 and age >= 17:
    print("고등학생")
elif age < 17 and age >= 14:
    print("중학생")
elif age < 14 and age >= 8:
    print("초등학생")
else:
    print("학생이 아님")