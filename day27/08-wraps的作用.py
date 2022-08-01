# 作者: Michael(phb)
# 2022年06月29日21时33分14秒
from functools import wraps


def my_decorator(func):
    @wraps(func)  # 让函数显示自己的名字和备注
    def wper(*args, **kwargs):
        '''decorator doc'''
        print('calling decorated function')
        return func(*args, **kwargs)

    return wper


@my_decorator
def example():
    '''example doc'''
    print('calling example function')


print(example.__name__, example.__doc__)
example()
