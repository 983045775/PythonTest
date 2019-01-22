class Gun:
    """枪"""

    def __init__(self, module):
        self.module = module
        self.bullet = None

    def add_bullet(self, count):
        self.bullet = count

    def shoot(self):
        if self.bullet <= 0:
            print("请加个子弹先")
            return
        self.bullet -= 1
        print("%s发射突突突突突突   ---   还剩%s发" % (self.module, self.bullet))


class Soldiers:
    """士兵"""

    def __init__(self, name):
        self.name = name
        self.gun = None

    def setGun(self, gun):
        self.gun = gun

    def fire(self, count):
        if self.gun is None:
            print("%s请上个枪先" % self.name)
            return
        print("开枪!")
        self.gun.add_bullet(count)
        self.gun.shoot()


an94_gun = Gun("AN94")

lc_soldiers = Soldiers("lc")

lc_soldiers.setGun(an94_gun)
lc_soldiers.fire(11)
