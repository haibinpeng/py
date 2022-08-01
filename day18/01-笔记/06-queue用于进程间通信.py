# 作者: Michael(phb)
# 2022年06月19日22时31分44秒
from multiprocessing import Process, Queue
import time


def writer(q: Queue):
    for i in ['A', 'B', 'C']:
        print('I am writing')
        q.put(i)
        time.sleep(1)


def reader(q: Queue):
    while True:
        if not q.empty():
            data = q.get()
            print(f'Get {data} from queue')
            time.sleep(2)
        else:
            break


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=writer, args=(q,))
    pw.start()
    time.sleep(1)  # 确保写完了
    pr = Process(target=reader, args=(q,))
    pr.start()
    pw.join()
    pr.join()
