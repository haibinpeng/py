# 作者: Michael(phb)
# 2022年06月28日23时25分49秒
def set_func(func):
    print('--开始进行装饰--')

    def call_func(*args, **kwargs):
        print('---权限验证---')
        func(*args, **kwargs)

    return call_func


@set_func
def test1(num):
    print("-----test1---- {}".format(num))


test1(3)
