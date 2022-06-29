def open_r():
    # r+:读写,文件的指针将会放在文件的开头，若如果文件不存在，抛出异常
    file = open('Readme', 'r+', encoding='utf8')
    file.write('帅')
    file.close()


def open_w():
    # w+:读写,如果文件存在会被覆盖；如果文件不存在，创建新文件
    f = open('Readme', 'w+', encoding='utf8')
    f.write("hello python！\n")
    f.write("今天天气真好")
    f.close()


def open_a():
    # a+:读写，如果该文件已存在，文件指针将会放在文件的结尾；如果文件不存在，创建新文件
    f = open('Readme', 'a+', encoding='utf8')  # a：追加模式
    f.write('\n哈哈')
    f.close()


if __name__ == '__main__':
    # open_r()
    # open_w()
    open_a()
