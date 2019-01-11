"""

剪刀石头布 ,1是剪刀 2是石头 3是布

"""
import random

while True:
    player = int(input("出拳吧, 1是剪刀 2是石头 3是布"))
    conputer = random.randint(1, 3)

    if ((player.__eq__(1) and conputer.__eq__(3))
            or (player.__eq__(2) and conputer.__eq__(1))
            or (player.__eq__(3) and conputer.__eq__(2))):
        print("玩家获胜了,电脑出的%d" % conputer)
    elif player.__eq__(conputer):
        print("平局,电脑出的%d" % conputer)
    else:
        print("电脑获胜,电脑出的%d" % conputer)
