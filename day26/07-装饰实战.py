# 作者: Michael(phb)
# 2022年06月28日23时25分49秒

# 定义函数：完成包裹数据
def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"

    return wrapped


# 定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


@makeBold
@makeItalic
def test():
    return 'hello-world-3'


print(test())
