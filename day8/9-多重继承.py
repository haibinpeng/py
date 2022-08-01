class A:
    def test(self):
        print('A test')

    def demo(self):
        print('A demo')


class B:
    def test(self):
        print('B test')

    def demo(self):
        print('B demo')

    def demo2(self):
        print('B demo2')


class C(A, B):  # 多重继承
    def demo(self):
        print('C demo')


c = C()
print(C.__mro__)  # 可以查看继承顺序
c.demo()
c.test()
c.demo2()
