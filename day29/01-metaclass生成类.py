# 作者: Michael(phb)
# 2022年07月01日19时28分48秒
class UpperAttrMetaClass(type):
    def __new__(cls, class_name, class_parent, class_attr: dict):
        new_attr = {}
        for name, value in class_attr.items():
            if not name.startswith('__'):
                new_attr[name.upper()] = value

        return type.__new__(cls, class_name, class_parent, new_attr)


class Foo(metaclass=UpperAttrMetaClass):
    bar = 'bip'


class FooChild(Foo):
    pass


print(Foo.BAR)
print(FooChild.BAR)
