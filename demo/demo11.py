peple = {"name": "lc",
         "age": "23",
         "location": "hf",
         "job": "android"}

# 拿到所有的key值 转成列表可以增删改查操作
peplo_tuple = tuple(peple.keys())

# 可遍历的(键, 值),拿到转成列表,且为二维数组
people_items = list(peple.items())
# 弹出指定key
peple_name = peple.pop("name")
# copy出新字典
peple_copy = peple.copy()
# 清空
# peple.clear()

# 创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值
seq = ('name', 'age', 'sex')
print(str(peple.fromkeys(seq, "13")))
# 根据key找value
print(peple.get("age"))
# 随机返回并删除字典中的一对键和值
print(peple.popitem())
# 如果键不存在于字典中，将会添加键并将值设为default
peple.setdefault("aaa", "bbb")
# 将其他的字典添加到peple中,如果已有则替代
peple.update()
# 取出所有的value
print(list(peple.values()))
print(peple_copy)

print(peple_name)
print(people_items[1][0])

print(people_items)
print(peple.items())

print(peple)
