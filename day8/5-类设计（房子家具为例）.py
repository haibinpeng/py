class HouseItem:
    """家具类"""

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return '[%s]占地%.2f' % (self.name, self.area)


# 创建家具对象
bed = HouseItem('席梦思', 4)
chest = HouseItem('衣柜', 2)
table = HouseItem('餐桌', 1.5)

print(bed)
print(chest)
print(table)

print('-' * 50)


class House:
    """房子类"""

    def __init__(self, area):
        self.area = area
        # 剩余面积
        self.free_area = area  # 初始就为area
        # 家具名称列表
        self.item_list = []

    def __str__(self):
        return f'总面积{self.area}，家具{self.item_list}，剩余面积{self.free_area}'

    def add_item(self, item: HouseItem):
        print(f'将要添加{item}')
        if self.free_area < item.area:
            print('面积不够，添加失败')
            return
        self.item_list.append(item.name)
        self.free_area -= item.area


# 创建房子对象
my_home = House(7)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)
