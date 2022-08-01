class Tool:
    count = 0  # 类属性，使用赋值语句定义类属性，记录创建工具对象的总数

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool('斧头')
tool2 = Tool('榔头')
tool3 = Tool('铁锹')
tool3.count = 99
print(tool3.count)
print(f'创建了{Tool.count}个工具')  # 对象.类属性=值的赋值语句，只会给对象添加一个属性，而不会影响到类属性的值
