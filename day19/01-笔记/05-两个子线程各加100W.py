# 作者: Michael(phb)
# 2022年06月20日21时50分46秒
import threading

num = 0


class MyThread(threading.Thread):
    def run(self):
        global num
        for i in range(1000000):
            num += 1


if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)
