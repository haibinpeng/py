# 作者: Michael(phb)
# 2022年06月18日00时20分34秒
import time
from multiprocessing import Process


def run_proc():
    while True:
        print('---2---')
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=run_proc)
    p.start()
    while True:
        print('---1---')
        time.sleep(1)
