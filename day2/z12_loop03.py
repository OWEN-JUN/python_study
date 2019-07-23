# 키보드 입력수 만큼 반복

count =0
count = int(input("반복값 입력>>"))
for i in range(1, count+1):
    print(i, end=" ")
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

i = 0;s = 0 ; e = 0;

s = int(input("반복 시작값 >>"))
e = int(input("반복 끝값 >>"))
for i in range(s, e+1):
    print(i, end=" ")
