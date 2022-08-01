# 作者: Michael(phb)
# 2022年06月21日22时30分44秒
from gevent import monkey
import gevent
import random

monkey.patch_all()


def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        gevent.sleep(random.random())  # 模拟I/O阻塞时间不确定


gevent.joinall([
    gevent.spawn(coroutine_work, "work1"),
    gevent.spawn(coroutine_work, "work2")
])
