# 作者: Michael(phb)
# 2022年06月19日20时06分19秒
from multiprocessing import Process
import os
import time

nums = [1, 2]


def func1():
    print(f'in process1 pid={os.getpid()}, {nums}')
    for i in range(3, 6):
        nums.append(i)
        time.sleep(1)
        print(f'in process pid={os.getpid()}, {nums}')


if __name__ == '__main__':
    p = Process(target=func1)
    p.start()
    p.join()
    print(f'执行子进程后：{nums}')  # 创建的子进程是自己的复制，子进程里对全局变量的修改不会影响父进程
