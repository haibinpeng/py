# 作者: Michael(phb)
# 2022年06月19日19时27分13秒
from multiprocessing import Process
import os
import time


def run_proc():
    print(f'子进程pid:{os.getpid()}')
    print(f'我的父进程pid:{os.getppid()}')
    while True:
        time.sleep(1)


if __name__ == '__main__':
    print(f'父进程pid:{os.getpid()}')
    p = Process(target=run_proc)
    p.start()
    p.join(3)  # 等待子进程结束或指定时间，回收子进程
    p.terminate()  # 不管任务是否结束，立即终止子进程
    p.join()
