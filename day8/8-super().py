class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")


class Dog(Animal):  # 单继承
    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print('飞---')

    def bark(self):  # 重写，针对子类特有的需求，编写代码
        print('我是哮天犬！')
        # 使用super().调用原本在父类中封装的方法
        super().bark()  # 使用super()时，实际传入的是孩子的对象，使用了父亲的方法


zizi = XiaoTianQuan()
zizi.eat()
zizi.fly()
zizi.bark()
