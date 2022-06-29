# 作者: Michael(phb)
# 2022年06月26日21时28分14秒
class Animal:

    def eat(self):
        pass

    def voice(self):
        pass


class Dog(Animal):
    def eat(self):
        print('狗吃骨头')

    def voice(self):
        print('狗叫汪汪')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

    def voice(self):
        print('猫叫喵喵')


class FactoryMode:
    def __init__(self):
        self.factory = {'dog': Dog, 'cat': Cat}

    def create_animal(self, animal_name):
        return self.factory[animal_name]()  # 返回的是一个类


f = FactoryMode()
animal = f.create_animal('dog')
animal.eat()
animal.voice()
