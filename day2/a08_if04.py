#if~elif~elif.........~else

score = int(input("총점입력 >>"))

hakjum = ''

if score >= 90:
    hakjum = "A"
elif score >= 80:
    hakjum = "B"
elif score >= 70:
    hakjum = "C"
elif score >= 60:
    hakjum = "D"
else:
    hakjum = "F"

print("총점 : %d \n학점 : %s" % (score, hakjum))