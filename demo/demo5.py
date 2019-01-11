# 99乘法表
i = 0

while i < 9:
    i += 1
    j = 0
    while j < i:
        j += 1
        if (j == 3 and i == 3) or (j == 3 and i == 4):
            print(" %dx%d=%d " % (j, i, i * j), end="")
        else:
            print("%dx%d=%d " % (j, i, i * j), end="")
    print("")
