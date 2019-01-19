# 缺省参数函数练习

def calculation_peplo(name, age=18, sex=True):
    sex_peplo = "男"
    if not sex:
        sex_peplo = "女"

    print("%s今年的年龄是%d,性别是%s" % (name, age, sex_peplo))


penson = "dsadadadad"
penson.format(3, 3, 3, 3, 3, 3, 3)
print(penson)
calculation_peplo("小明")
calculation_peplo("小妹", age=1, sex=False)
calculation_peplo("小猪", age=213)
