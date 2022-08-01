# 作者: Michael(phb)
# 2022年07月01日22时26分55秒
from abc import abstractmethod, ABCMeta


class Person(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


# p = Person()  # 不能对抽象类本身实例化
class P1(Person):
    def walk(self):
        print('walk1')

    def sleep(self):
        print('sleep1')


class P2(Person):
    def walk(self):
        print('walk2')

    def sleep(self):
        print('sleep2')


p1 = P1()
p2 = P2()
p1.walk()
p2.sleep()
