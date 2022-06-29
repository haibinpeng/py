# 作者: Michael(phb)
# 2022年06月20日20时30分09秒
import threading
from time import sleep,ctime


def sing():
    for i in range(5):
        print("正在唱歌...%d" % i)
        sleep(1)


def dance():
    for i in range(5):
        print("正在跳舞...%d" % i)
        sleep(1)


if __name__ == '__main__':
    print('---开始---:%s' % ctime())
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    # exit(1)  # exit让主线程终止了，但是还是会等子线程
    t1.join()
    t2.join()
    print('---结束---:%s' % ctime())
