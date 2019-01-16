# 切片练习

import re

num_str = str(list(range(99)))
# 过滤模式创建
p = re.compile(r'[^0-9]')
num_str = re.sub(p, "", num_str)

# 截取2到5的字符串
print("\r\n" + num_str[2:6] + "\r\n", end="-" * 40)
# 截取2到末尾的字符
print("\r\n" + num_str[2:] + "\r\n", end="-" * 40)
# 截取0到5的数字
print("\r\n" + num_str[:6] + "\r\n", end="-" * 40)
# 截取完整的字符串
print("\r\n" + num_str[:] + "\r\n", end="-" * 40)
# 每隔一个取一个
print("\r\n" + num_str[::2] + "\r\n", end="-" * 40)
# 索引1开始每隔一个取一个
print("\r\n" + num_str[1::2] + "\r\n", end="-" * 40)
# 截取从2到末尾-1的字符串
print("\r\n" + num_str[2:-1] + "\r\n", end="-" * 40)
# 截取末尾两个字符
print("\r\n" + num_str[-2:] + "\r\n", end="-" * 40)
# 字符串的逆序输出

print("\r\n" + num_str[::-1] + "\r\n", end="-" * 40)
print("\r\n" + num_str)
