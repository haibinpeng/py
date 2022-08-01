# 作者: Michael(phb)
# 2022年06月19日23时23分38秒
import time
from threading import Thread


def say_hello():
    print('hello')
    time.sleep(1)


if __name__ == '__main__':
    for i in range(5):
        t = Thread(target=say_hello)
        t.start()
