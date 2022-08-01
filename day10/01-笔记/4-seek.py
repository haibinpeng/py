import os


def use_seek1():
    f = open('Readme', 'r+', encoding='utf8')
    f.seek(6, os.SEEK_SET)  # 相对于开头偏移6个字节
    test = f.read()
    print(test)


def use_seek2():
    """偏移到结尾，从尾部接着写"""
    f = open('Readme', 'r+', encoding='utf8')
    f.seek(0, os.SEEK_END)  # 偏移到文件尾部
    f.write('\nhi')
    f.close()


if __name__ == '__main__':
    # use_seek1()
    use_seek2()
