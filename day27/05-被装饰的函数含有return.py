# 作者: Michael(phb)
# 2022年06月29日18时04分49秒
from time import ctime


def time_func(func):
    def wrapped_func():
        print(f'{func.__name__} called at {ctime()}')
        # func()  # None
        return func()  # 一般情况下为了让装饰器更通用，加上return

    return wrapped_func


@time_func
def get_info():
    return '这是一个重要任务'


print(get_info())
