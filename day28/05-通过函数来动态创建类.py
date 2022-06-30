# 作者: Michael(phb)
# 2022年06月30日21时45分27秒
def create_class(name):
    if name == 'foo':
        class Foo:
            pass

        return Foo
    else:
        class Bar:
            pass

        return Bar


my_class = create_class('foo')
print(my_class)
my_class = create_class('bar')
print(my_class)
