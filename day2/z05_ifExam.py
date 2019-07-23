#공원 입장료 6세 이하 , 70세 이상 무료 나머지 5000

cost = 0
age = int(input("나이를 입력하세요 >>"))

if age <= 6 or age >= 70:
    cost = 0
    print("무료입장입니다.")
    print("입장료 : %d원"% cost )
else:
    cost = 5000
    print("유료입장입니다.")
    print("입장료 : %d원" % cost)