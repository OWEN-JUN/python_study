#사용자가 입력한 정수값이 1~100 인지 판단
#0이하이거나 100초과이면 0으로 처리
user_num = int(input("정수값을 입력하세요(1~100)"))

if user_num >= 1 and user_num <= 100:
    print(user_num, "1~100사이의 정수입니다.")
else:
    user_num = 0
    print(user_num, "이 1~100사이가 아니므로 0으로 처리!")