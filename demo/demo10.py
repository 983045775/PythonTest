# 元祖练习

# 定义元祖

data_tuple = ("zhangsan", 3, 12.3)

# 第一次出现的位置
first_index = data_tuple.index(3)
print("第一次出现的位置 %d" % first_index)
# 出现了多少次
data_tuple.count(3)
# 转列表
data_list = list(data_tuple)

# 转成元祖 tuple
convert_tuple = tuple(data_list)
data_list[2] = 21341
print(type(data_list))
print(data_list)

print()
print(type(data_tuple))
print(data_tuple)

print(data_tuple[2])
print("\n\n\n", end="")
# 遍历列表和元祖

for item in convert_tuple:
    print(item)

for item in data_list:
    print(item)
