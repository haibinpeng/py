# 作者: Michael(phb)
# 2022年06月29日17时52分26秒
from time import ctime, sleep


def time_func(func):
    def wrapped_func():
        print(f'{func.__name__} called at {ctime()}')
        func()

    return wrapped_func


@time_func
def foo():
    print('I am foo')


foo()
sleep(2)
foo()
