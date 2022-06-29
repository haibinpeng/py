# 作者: Michael(phb)
# 2022年06月28日23时17分05秒
def set_func(func):
    def call_func():
        print('权限验证')
        func()

    return call_func


@set_func
def test():
    print('test')


# test = set_func(test)  # 这就是@做的事
test()
