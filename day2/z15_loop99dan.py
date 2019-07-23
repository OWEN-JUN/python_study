

print("@@@@@@@구구단@@@@@@@")
for i in range(2, 10):
    print("~~~~~%d단~~~~~" %i)
    for j in range(1, 10):
        print("%d * %d = %2d" %(i, j, i * j))







print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


for i in range(1, 10):

    for j in range(1, 10):
        print("%2d * %d = %3d" %(j, i, j * i), end="      ")

    print()
print()
for i in range(1, 10):

    for j in range(10, 16):
        print("%2d * %d = %3d" %(j, i, j * i), end="      ")
    print()