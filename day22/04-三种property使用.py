# 作者: 王道 龙哥
# 2022年06月23日10时04分38秒
class Goods:
    @property
    def price(self):
        print('@property')

    @price.setter
    def price(self, value):
        print('@price.setter')

    @price.deleter
    def price(self):
        print('@price.deleter')


obj = Goods()
obj.price  # 自动执行@property修饰的price方法，并获取方法的返回值
obj.price = 123  # 自动执行@price.setter修饰的price方法，并将123赋值给方法的参数
del obj.price  # 自动执行@price.deleter修饰的price方法
