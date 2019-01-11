# 偶数求和
i = 0
count = 0

while i < 100:
    i += 1
    if not (i % 2 == 1):
        if 90 > i > 10:
            break
        print("i的值是%d" % i)
        count += i

print("最后的值是%d" % count)
