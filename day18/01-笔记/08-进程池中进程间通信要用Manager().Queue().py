# 作者: Michael(phb)
# 2022年06月19日22时39分18秒
from multiprocessing import Pool, Manager
import time


def writer(q):
    for i in ['A', 'B', 'C']:
        print('I am writing')
        q.put(i)
        time.sleep(1)


def reader(q):
    while True:
        if not q.empty():
            data = q.get()
            print(f'Get {data} from queue')
            time.sleep(2)
        else:
            break


if __name__ == '__main__':
    po = Pool(3)
    q = Manager().Queue()
    po.apply_async(writer, (q,))
    time.sleep(1)
    po.apply_async(reader, (q,))
    po.close()
    po.join()
