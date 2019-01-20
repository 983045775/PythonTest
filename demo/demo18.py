class Cat:

    def drink(self):
        print("喝")

    def eat(self):
        print("吃")


class Dog:
    # 构造函数
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "重写了toString方法"

    def __del__(self):
        print("已销毁, 清理各种引用对象,释放内存")

    def eat(self):
        print("它叫%s,正在吃" % self.name)

    def drink(self):
        print("%s会喝" % self.name)


pis_cat = Cat()

pis_cat.drink()
pis_cat.eat()

print(pis_cat)

print(dir(pis_cat))

jack_dog = Dog("jack")

jack_dog.eat()
jack_dog.drink()
print(jack_dog)
