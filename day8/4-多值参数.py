# 多值参数
def sum_numbers(*args):
    num = 0
    # 遍历args元组顺序求和
    for n in args:
        num += n
    return num


print(sum_numbers(1, 2, 3))

print('-' * 50)


def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


if __name__ == '__main__':
    # demo(1, 2, 3, 4, 5, name='Michael', age=18, gender=True)
    tuple1 = (1, 2, 3, 4, 5)
    dict1 = {'name': 'Michael', 'age': 18, 'gender': True}
    # 元组拆包，把一个元组变为调用函数时实参传递的样子
    # 字典拆包，把一个字典变为调用函数时keyword实参传递的样子
    demo(*tuple1, **dict1)  # 拆包后相当于demo(1, 2, 3, 4, 5, name='Michael', age=18, gender=True)
    # demo(*tuple1[::-1], **dict1)
