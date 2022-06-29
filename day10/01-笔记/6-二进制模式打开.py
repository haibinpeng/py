def open_b_read():
    f = open('Readme', 'rb+')
    btext = f.read()
    print(btext)


def open_b_write():
    f = open('Readme', 'rb+')
    # f.write(b'abc')  # 二进制写文件流
    f.write('烫'.encode('utf8'))  # 转为文件流
    f.close()


if __name__ == '__main__':
    # open_b_read()
    open_b_write()
