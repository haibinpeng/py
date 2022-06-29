# 作者: Michael(phb)
# 2022年06月26日22时35分46秒
class Foo:
    def func(self):
        print('I am func')

    @property
    def prop(self):
        print('I am prop')


f = Foo()
f.func()
f.prop  # 这是一个property属性

print('-' * 50)


class Goods:
    @property
    def size(self):
        return 100


desk = Goods()
width = desk.size
print(width)
