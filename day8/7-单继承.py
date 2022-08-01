class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):  # 单继承
    def bark(self):
        print("汪汪叫")


zizi = Dog()
zizi.eat()  # 从父类继承下来的
