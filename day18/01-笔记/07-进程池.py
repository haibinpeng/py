# 作者: Michael(phb)
# 2022年06月19日23时04分24秒
from multiprocessing.pool import Pool
import time
import os
import random


def worker(msg):
    t_start = time.time()
    print(f'{msg}开始执行，进程号为{os.getpid()}')
    time.sleep(random.random() * 2)  # 模拟
    t_end = time.time()
    print(f'{msg}执行完毕，耗时{(t_end - t_start):.2f}')


if __name__ == '__main__':
    po = Pool(3)
    for i in range(10):
        po.apply_async(worker, (i,))
    print('start')
    po.close()  # 关闭Poll，不再接受新任务
    # po.terminate()  # 不管任务是否完成，立即终止
    print('close后')
    po.join()  # 等待任务执行完成后子进程退出
    print('end')
