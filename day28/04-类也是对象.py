# 作者: Michael(phb)
# 2022年06月30日21时22分36秒
class ObjectCreator:
    pass


def echo(obj):
    print(obj)
    obj.new_attribute = 'foo'  # 可以增加属性
    print(obj())  # 通过ObjectCreator做了一个实例对象


echo(ObjectCreator)  # 可以作为函数参数进行传递
print(ObjectCreator.new_attribute)  # 可以增加属性
print(hasattr(ObjectCreator, 'new_attribute'))  # hasattr可以判断某个类中是否有某个属性
