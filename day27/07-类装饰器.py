# 作者: Michael(phb)
# 2022年06月29日21时07分08秒
# 装饰器函数其实是这样一个接口约束:它必须接受一个callable对象作为参数，然后返回一个callable对象。在Python中一般callable对象都是函数，
# 但也有例外，只要某个对象重写了__call__（）方法，那么这个对象就是callable的
class Test:
    def __init__(self, func):
        print(f'func name is {func.__name__}')
        self.func = func

    def __call__(self, *args, **kwargs):
        print('这是个验证')
        return self.func(*args, **kwargs)


@Test  # 相当于test = Test(test)
def test():
    print('test')


test()
