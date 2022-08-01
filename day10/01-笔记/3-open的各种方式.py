def open_r_add():
    # file = open('Readme', 'r', encoding='utf8')  # r:只读
    file = open('Readme', 'r+', encoding='utf8')  # r+:读写
    file.write('帅')  # 只读模式下不能写。utf8模式下1个汉字是3个字节
    file.close()


def open_w():
    # 打开 - 文件存在，就清空，不存在，就创建
    f = open('Readme', 'w', encoding='utf8')
    f.write("hello python！\n")
    f.write("今天天气真好")
    f.close()


def read_line():
    """一次读一行，读空文件"""
    f = open('Readme', 'r+', encoding='utf8')
    while True:
        text = f.readline()
        if not text:
            break
        # 每读取一行的末尾已经有了一个`\n`
        print(text, end='')


def open_a_read():
    f = open('Readme', 'a+', encoding='utf8')  # a：追加模式
    text = f.read()  # 追加模式光标在最后，再读什么读不到
    print(text)
    f.close()


def open_a_write():
    f = open('Readme', 'a+', encoding='utf8')
    f.write('\n学习是一个持续的过程')
    f.close()


if __name__ == '__main__':
    # open_r_add()
    # open_w()
    # read_line()
    open_a_read()
    # open_a_write()
