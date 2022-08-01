# 作者: Michael(phb)
# 2022年06月20日21时39分29秒
import threading
import time


class MyThread(threading.Thread):
    def run(self):
        """重写run"""
        for i in range(3):
            time.sleep(1)
            print(self.name + ' @ ' + str(i))


def test():
    for i in range(3):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    test()  # 多线程程序的执行顺序是不确定的
