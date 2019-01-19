def result_person(name):
    age = 0
    height = 0
    if name.__eq__("lc"):
        age = 10
        height = 94.5
    elif name.__eq__("小明"):
        age = 20
        height = 182.3

    return age, height


def change_person(person):
    # 因为是列表所以,可以修改内存 and 字典也是同样的
    person.remove(2)


def sum_number(*args):
    # 求和
    # *args 一个*是列表
    # **kwargs 两个**是字典
    sum_result = 0
    for num in args:
        sum_result += num

    return sum_result


def sum_list(lists, new_list):
    # 实际是修改内存,走了extend方法
    lists += new_list


def print_person(name="lc", age=18, height=180.3):
    print("姓名%s年龄是%d身高是%.2fcm" % (name, age, height))


s_name = "小明"
s_age, s_height = result_person(s_name)

print("%s的身高是%s还有他的年龄是%s" % (s_name, s_height, s_age))

a = 111
b = 222

a = a + b
b = a - b
a = a - b

print("%d和%d" % (a, b))

person_list = [1, 2, 3, 4, 5, 6, 7, 8]
change_person(person_list)
print(person_list)

print(sum_number(1, 2, 3, 5, 6, 7, 8, 9, 0, 12, 2, 2))

num_list = [1, 2, 3]
new_list = [4, 5, 6]
sum_list(num_list, new_list)
print(num_list)
print_person(age=2555)
