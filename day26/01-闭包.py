# 作者: Michael(phb)
# 2022年06月28日22时15分42秒
def line(k, b):
    def create_y(x):
        print(k * x + b)

    return create_y


line_1 = line(1, 2)  # line_1是create_y闭包的入口地址
line_1(0)
line_1(1)

line_2 = line(3, 5)
line_2(0)
line_2(1)
