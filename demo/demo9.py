# 列表练习
name_list = ["zhangsan", "zhangsan2", "zhangsan3", "zhangsan4"]

# 删
name_list.remove("zhangsan2")
# 增
name_list.append("末尾增加")
del name_list[2]
# 改
name_list[0] = "zhangsan0"
# 查
print(name_list[1])

print(name_list)

exercise_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
# 删除
exercise_list.remove("2")
# 末尾追加
exercise_list.append("11")
# 计数出现次数
print("11出现的次数是:%d次" % exercise_list.count("11"))
# 清空
# exercise_list.clear()
# copy出一个新列表
copy_list = exercise_list.copy()
# 将一个列表添加到另一个列表中
exercise_list.extend(copy_list)
# 返回指定元素第一次出现的下标
print(exercise_list.index("3"))
# 在指定的下标插入元素
exercise_list.insert(3, "insert")
# 删除指定下标,且返回这个元素
print(exercise_list.pop(3))
# 反转
exercise_list.reverse()
# 排序
exercise_list.sort()
# 反排序
exercise_list.sort(reverse=True)
print(copy_list)
print(exercise_list)
