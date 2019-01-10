#测试
import keyword

qq_number = str(983045775)
qq_password = str(int(21.3241241231232131321))

print(qq_number + qq_password * 2)
apple_money = 15
size = 4

all_money = size * apple_money

all_money = all_money - 5
print(all_money)

isri = True

print(type(2 * 111.0))
print(2 + True)

print(str(qq_number) + "" + str(qq_password))

print(input("请输入"))

print(bool(size))

apple_size = int(input("输入数量"))
a_money = float(input("输入价格"))

print("价格是: ,%%" % (apple_size * a_money))

name = "小明";
print("我的名字叫%s,请多多指教" % name)

student_code = 1
print("我的学号是%09d" % student_code)

mon = 9.00
si = 14.00
Si = 14.00
zhi = 45.00

print("购买了%.2f元,具体是%.2f斤,花费了%.2f" % (mon, si, zhi))

percentage = .1
print("百分之%.2f%%" % (percentage * 100))

print(keyword.kwlist)

age = 18;

# not==! 取反    or==|| 或者    and==&& 并且
if not (age <= int(input("输入年龄"))):
    print("成人了");
else:
    print("还没有成人哦");

get_age = int(input("输入年龄哦"))

if 0 < get_age < 120:
    print(get_age)
else:
    print("年龄超过限制")

python_score = int(input("输入python成绩"))
c_score = int(input("输入c成绩"))

if python_score > 60 or c_score > 60:
    print("成绩合格")
else:
    print("不合格")

is_emloyee = int(input("输入是否是员工 0 和 1 代替"));
if not is_emloyee:
    print("允许进")
elif is_emloyee:
    print("不允许进")

holiday_name = input("女朋友的节日")
if holiday_name.__eq__("情人节"):
    print("买玫瑰")
elif holiday_name.__eq__("平安夜"):
    print("买苹果")
elif holiday_name.__eq__("生日"):
    print("买蛋糕")
else:
    print("每天都是节日")

has_ticket = int(input("0代表没有车票,1代表有车票"))

if has_ticket:
    knife_length = int(input("刀的长度"))
    if knife_length < 20:
        print("可以上车哦")
    else:
        print("不可以上车哦,刀太长了,有%.2fcm\r\n那么长" % knife_length)
else:
    print("不能进站")
