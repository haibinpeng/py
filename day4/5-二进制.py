#  统计一个整数对应的二进制数的1的个数
def count(num):
    if num >= 0:
        num_bin = bin(num)
        return num_bin.count('1')
    else:
        num = abs(num)
        num_bin = bin(num - 1)
        return 64 - num_bin.count('1')


print(count(int(input('请输入一个整数：'))))