# 作者: Michael(phb)
# 2022年06月29日18时01分44秒
def set_func(func):
    def call_func(*args, **kwargs):
        print("---这是权限验证1----")
        print("---这是权限验证2----")
        func(*args, **kwargs)  # 拆包

    return call_func


@set_func
def test1(num, *args, **kwargs):
    print("-----test1----%d" % num)
    print("-----test1----", args)
    print("-----test1----", kwargs)


test1(100)
test1(100, 200)
test1(100, 200, 300, m=100)
