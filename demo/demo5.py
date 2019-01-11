# 99乘法表
i = 0

while i < 9:
    i += 1
    j = 0
    while j < i:
        j += 1
        print("%dx%d=%d\t" % (j, i, i * j), end="")
    print("")
