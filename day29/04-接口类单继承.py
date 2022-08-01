# 作者: Michael(phb)
# 2022年07月01日22时18分23秒
class Alipay:
    def pay(self, money):
        # def paying(self, money):
        print('支付宝支付了')


class Applepay:
    def pay(self, money):
        print('苹果支付了')


class Weicht:
    def pay(self, money):
        print('微信支付了')


# 支付函数，总体负责支付，对应支付的对象和要支付的金额
def pay(payment, money):
    payment.pay(money)


p = Alipay()  # 一旦里边没有pay方法会报错
pay(p, 200)
