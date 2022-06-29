# 作者: Michael(phb)
# 2022年06月26日21时41分35秒
class Parent:
    def __init__(self, name):
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')


class Son(Parent):
    def __init__(self, name, age):
        print('Son1的init开始被调用')
        super().__init__(name)
        self.age = age
        print('Son1的init结束被调用')


# 属性如果没有执行self.xxx 就没有xxx属性
lisi = Son('lisi', 28)
print(lisi.name)
print(lisi.age)
