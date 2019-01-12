# 99乘法表
def mult_tab():
    i = 0

    while i < 9:
        i += 1
        j = 0
        while j < i:
            j += 1
            print("%d x %d = %d\t" % (j, i, i * j), end="")
        print("")


def say_h():
    print("h")


print("h")

