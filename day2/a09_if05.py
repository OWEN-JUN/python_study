#중첩 if

weather = input("오늘의 날씨는? >>")

if weather == "good":
    car = input("대중교통 종류?")

    if car =="bus":
        print("버스를 타고 있다.")
    else:
        print('버스를 타지 않았다.')

elif weather == "bad":
    print("대중교통을 이용하지 않음")