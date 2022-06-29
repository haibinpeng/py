# 作者: Michael(phb)
# 2022年06月29日17时59分04秒
from time import ctime, sleep


def time_func(func):
    def wrapped_func(a, b):  # 和func的参数个数保持一致
        print(f'{func.__name__} called at {ctime()}')
        func(a, b)

    return wrapped_func


@time_func
def foo(a, b):
    print(a + b)


foo(3, 5)
sleep(2)
foo(2, 4)
