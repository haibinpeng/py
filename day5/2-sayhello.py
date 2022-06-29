def say_hello(num):
    """
    打印hello
    """
    for i in range(num):
        print('hello')


num1 = int(input('请输入要打印的次数：'))
say_hello(num1)