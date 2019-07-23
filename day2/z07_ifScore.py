#국어 영어 수학 총점, 평균, 학점
print("@@@@@@@@@@@@@@@@@@@@성적프로그램@@@@@@@@@@@@@@@@@@@@")
kor = int(input("국어 점수를 입력하세요>>"))
eng = int(input("영어 점수를 입력하세요>>"))
math = int(input("수학 점수를 입력하세요>>"))
total = kor + eng + math
avg = total / 3
hakjum =''

if avg <= 100 and avg >= 90:
    hakjum = "A"
elif avg <= 89 and avg >= 80:
    hakjum = "B"
elif avg <= 79 and avg >= 70:
    hakjum = "C"
elif avg <= 69 and avg >= 60:
    hakjum = "D"
else:
    hakjum = "F"

print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("국어 : %d\n영어 : %d\n수학 : %d\n총점 : %d\n평균 %.1f\n학점 : %s학점" % (kor, eng, math, total, avg, hakjum))

