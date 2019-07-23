#1~100 합

sum = 0
for i in range(0, 101):
    sum += i

print("1~100까지의 합 : %d" % sum)


#500~1000사이의 홀수값 출력
total = 0
for i in range(500, 1001):
    if i % 2 != 0:
        print(i, end=' ')
        total += i
print("")
print(total)

#500~1000사이의 7의배수값 출력
total = 0
for i in range(500, 1001):
    if i % 7 == 0:
        print(i, end=" ")
        total += i

print("")
print(total)