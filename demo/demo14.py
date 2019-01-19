num = 10


def print_num():
    global num
    num = 99


def change_num():
    global num
    num = 77


print_num()
change_num()
print(num)

a = 11
b = 21

a = a + b
b = a - b
a = a - b

print(a)
print(b)
