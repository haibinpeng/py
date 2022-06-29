# 作者: Michael(phb)
# 2022年06月28日22时47分58秒
x = 300


def test1():
    x = 200

    def test2():
        # global x
        nonlocal x
        print("----1----x=%d" % x)
        x = 100  # 一旦修改就必须加修饰
        print("----2----x=%d" % x)

    return test2


t = test1()
t()


# 外部函数的形参也是nonlocal类型
def counter(start):
    def incr():
        nonlocal start
        start += 1
        return start

    return incr


c1 = counter(5)
print(c1())
print(c1())
