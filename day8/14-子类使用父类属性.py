# 作者: Michael(phb)
# 2022年06月14日21时13分54秒
class A:
    def __init__(self):
        self.name = 'xiongda'

    def sleep(self):
        print('sleep')


class B(A):
    def __init__(self):
        super().__init__()  # 子类使用父类属性
        self.age = 10


b = B()
b.sleep()
print(b.name)
