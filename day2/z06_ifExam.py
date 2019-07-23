#bmi 즉정.BMI지수= 몸무게(kg) ÷ (신장(m) × 신장(m))
#18.5 이하 저체중
#18.6~24.9 정상
#25.0~29.9 과체중
#30.0 이상 비만

tall = int(input("당신의 키는 몇입니까(cm) >>"))
weight = float(input("당신의 몸무게는 몇입니까 >>"))

bmi = weight / ((tall/100)**2)
bmi = bmi.__round__(1)

if bmi <= 18.5:
    print("bmi : %.1f\n저체중입니다." % bmi)
elif bmi > 18.5 and bmi <=24.9:
    print("bmi : %.1f\n정상입니다." % bmi)
elif bmi >= 25.0 and bmi <=29.9:
    print("bmi : %.1f\n과체중입니다." % bmi)
else:
    print("bmi : %.1f\n비만입니다." % bmi)

