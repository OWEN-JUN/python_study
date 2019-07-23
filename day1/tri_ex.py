def drawdiamond(num):
    for i in range(1, num + 1):
        print(" " * (num - i),"*" * (2 * i - 1))
    for i in range(num - 1, 0, -1):
        print(" " * (num - i),"*" * (2 *i -1))


diamond = int(input("만들어질 다이아몬드 줄수>>"))
drawdiamond(diamond)

