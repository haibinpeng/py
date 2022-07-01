# 作者: Michael(phb)
# 2022年07月01日22时24分09秒
from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):
    @abstractmethod  # 抽象方法是需要子类来实现这个方法，如果子类中没有重写这个方法就报错
    def pay(self, money):
        pass


class Alipay(Payment):
    def paying(self, money):
        print('支付宝支付了')


class Apppay:
    def pay(self, money):
        print('苹果支付了')


class Weicht:
    def pay(self, money):
        print('微信支付了')


# 支付函数，总体负责支付，对应支付的对象和要支付的金额
def pay(payment, money):
    payment.pay(money)


p = Alipay()
