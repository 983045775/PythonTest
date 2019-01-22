class HouseFurniture:

    def __init__(self, name, area):
        self.name = name
        self.area = area
        print("买了一个%s面积是%.2f平米" % (name, area))

    def __str__(self):
        return "名字有%s " % self.name


class House:
    # 家具列表
    furniture_list = []

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        print("%s的房子,面积%.2f" % (house_type, area))

    def __str__(self):
        return "房子是%.2f大小,空余%.2f平米,家具有%s " % (self.area, self.free_area, ",".join(self.furniture_list))

    def add_furniture(self, furniture):
        if furniture.area > self.free_area:
            print("面积过大了,你这玩意%.2f那么大,空间就剩%.2f了" % (furniture.area, self.area))
            return
        self.furniture_list.append(furniture.name)
        self.free_area -= furniture.area


house = House("两室两厅", 83.22)

bedFurniture = HouseFurniture("床", 14.2)
cabinetFurniture = HouseFurniture("柜子", 12.7)
tableFurniture = HouseFurniture("桌子", 9.6)

house.add_furniture(bedFurniture)
house.add_furniture(cabinetFurniture)
house.add_furniture(tableFurniture)

print(house)
