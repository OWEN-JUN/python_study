x = 30; y = 40

print(x)
print("x =", x)
print("x + y =", x + y)

print("%d + %d = %d" % (x, y, (x+y)))
print("%d / %d = %.3f" % (x, y, (x / y)))

print("PI = %f" % (3.14))
print("PI = %.2f" % (3.14))

print("3.14는 %s이다" %("파이값"))

name = "owen"
print("제 이름은 %s" % name)
print("제 이름은 %s" % name[3])

print("제 이름은 %s" % name.lower())
print("제 이름은 %s" % name.upper())

check = name.__contains__("ow")

print(check)
