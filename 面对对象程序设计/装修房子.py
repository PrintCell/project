class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s 占地 %.1f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.leave_area = area
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n面积：%.1f\n家具种类：%s\n剩余面积: %.1f"
                % (self.house_type, self.area, self.item_list, self.leave_area))

    @staticmethod
    def add_item(item):
        print("要添加 %s" % item)
        if item.area >= my_house.leave_area:
            print("%s 太大，放不下" % item)
            return
        else:
            my_house.item_list.append(item.name)
            my_house.leave_area -= item.area
            print("%s添加成功" % item.name)
            print("剩余面积%.1f" % my_house.leave_area)


bed = HouseItem("席梦思", 40)
chest = HouseItem("柜子", 2)
table = HouseItem("餐桌", 1.5)
print(bed)
print(chest)
print(table)

# 创建房子对象
my_house = House("一室一厅", 40)
print(my_house)
my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)
