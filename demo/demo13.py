# 10 等于 2 * 5
# 11 是一个质数
# 12 等于 2 * 6
# 13 是一个质数
# 14 等于 2 * 7
# 15 等于 3 * 5
# 16 等于 2 * 8
# 17 是一个质数
# 18 等于 2 * 9
# 19 是一个质数
for num in range(10, 20):
    for remainder in range(2, num):
        if num % remainder == 0:
            print("%d 等于 %d * %d" % (num, remainder, num / remainder))
            break
    else:
        print("%d 是一个质数" % num)

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, [3, 4, 5]]
# 输出3到7
print(num_list[2:-2])

#TODO
seach_list = [3, 4, 5]

seach_bool = seach_list in num_list

print(seach_bool)
