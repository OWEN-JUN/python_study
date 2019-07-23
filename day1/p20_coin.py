#변수 선언부분
money = 0; c500=0; c100=0; c50=0; c10=0

#입력 및 처리 코드

money = int(input("교환할 돈을 입력하세요 >>"))
c500 = money // 500
money = money % 500
c100 = money // 100
money = money % 100
c50 = money // 50
money = money % 50
c10 = money // 10
money = money % 10

print("500원 : %d개 \n100원 : %d개 \n50원 : %d개 \n10원 : %d개\n" % (c500, c100, c50, c10))
print("남은 금액 >>> %d원" %money)