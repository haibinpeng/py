# 作者: Michael(phb)
# 2022年07月01日22时25分50秒
from abc import abstractmethod, ABCMeta


class Walk_animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass


class Swim_animal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass


class Fly_animal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class Tiger(Walk_animal, Swim_animal):
    def swim(self):
        print('tiger swim')

    def walk(self):
        print('tiger walk')


t1 = Tiger()
