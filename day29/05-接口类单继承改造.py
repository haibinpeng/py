# 作者: Michael(phb)
# 2022年07月01日22时22分08秒
class Payment:
    def pay(self, money):
        e = Exception('缺少编写pay方法')
        raise e  # 手动抛异常


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
pay(p, 200)
