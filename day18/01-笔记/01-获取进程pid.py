# 作者: Michael(phb)
# 2022年06月18日22时39分19秒
from multiprocessing import Process
import os


def run_proc():
    print(f'子进程pid:{os.getpid()}')
    print(f'我的父进程pid:{os.getppid()}')


if __name__ == '__main__':
    print(f'父进程pid:{os.getpid()}')  # os.getpid获取当前进程的进程号
    p = Process(target=run_proc)
    p.start()
