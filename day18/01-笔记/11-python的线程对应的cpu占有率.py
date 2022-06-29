# 作者: Michael(phb)
# 2022年06月19日23时27分23秒
from threading import Thread


def while1():
    while True:
        pass


if __name__ == '__main__':
    t = Thread(target=while1)
    t.start()
    while True:
        pass
