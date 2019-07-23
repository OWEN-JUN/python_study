#두수를 입력 받아 대소관계 비교

num1 = int(input("첫번째 수를 입력하시오\n"))
num2 = int(input("두번째 수를 입력하시오\n"))

if num1 > num2:
    print(num1, ">", num2)
elif num1 < num2:
    print(num1, "<", num2)
else:
    print(num1, "==", num2)