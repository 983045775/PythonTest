"""

剪刀石头布 ,1是剪刀 2是石头 3是布

"""
player = int(input("出拳吧, 1是剪刀 2是石头 3是布"))
conputer = int(input("电脑出拳吧"))

if ((player.__eq__(1) and conputer.__eq__(3))
        or (player.__eq__(2) and conputer.__eq__(1))
        or (player.__eq__(3) and conputer.__eq__(2))):
    print("玩家获胜了")
elif player.__eq__(conputer):
    print("平局")
else:
    print("电脑获胜")
