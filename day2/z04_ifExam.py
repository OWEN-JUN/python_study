#입력한 문자가 women, man 인지 판단

gender = input("성별입력 >>")

if gender == "women" or gender == "여성":
    print("여성입니다.")
elif gender == "man" or gender == "남성":
    print("남성입니다.")
else:
    print("잘못된 입력입니다.")