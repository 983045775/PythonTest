# 函数内修改引用, 只有 字典和列表是可变类型, 修改是直接针对内存地址修改, 而不是创建新的  让变量给引用
def change_num(num, num_list):
    new_num = num.lower()
    num_list.reverse()
    print(new_num)


num = "HAHAHA"
num_list = [4, 5, 6]

change_num(num, num_list)

print(num)
print(num_list)