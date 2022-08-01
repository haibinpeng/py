# 通过try进行异常捕捉，确保输入的内容一定是一个整型数，然后判断该整型数是否是对称数
try:
    str1 = input('请输入一个整型数:')
    num = int(str1)
    num1 = 0
    num2 = num
    while num2:
        num1 = num1 * 10 + num2 % 10
        num2 //= 10  # 整除
    if num1 == num:
        print(f'{num}是对称数')
    else:
        raise Exception(f'{num}不是对称数')
except ValueError:
    print('非整型')
except Exception as result:
    print(result)
