# 作者: Michael(phb)
# 2022年06月29日17时43分46秒
import time


def count_time(func):
    def call_func():
        start = time.time()
        func()
        end = time.time()
        print(f'use time = {end-start}')
    return call_func


@count_time
def test1():
    print('test')
    for i in range(1000000):
        pass


test1()
