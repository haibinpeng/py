import os


def write_read():
    f = open('Readme', 'r+', encoding='utf8')
    f.write('world')
    f.seek(0, os.SEEK_CUR)  # 刷新位置指针
    text = f.read(6)
    print(text)
    f.close()


def read_write():
    f = open('Readme', 'r+', encoding='utf8')
    text = f.read(6)
    print(text)
    f.seek(0, os.SEEK_CUR)  # 刷新位置指针
    f.write('java')
    f.close()


if __name__ == '__main__':
    # write_read()
    read_write()
