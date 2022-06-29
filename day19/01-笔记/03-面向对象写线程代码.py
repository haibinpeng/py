# 作者: Michael(phb)
# 2022年06月20日21时25分26秒
import threading
import time


class MyThread(threading.Thread):
    def run(self):
        """重写run"""
        for i in range(3):
            time.sleep(1)
            print(self.name + ' @ ' + str(i))  # name属性中保存的是当前线程的名字


if __name__ == '__main__':
    t = MyThread()
    t.start()  # start中调用了run
