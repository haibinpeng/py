import os


def use_dir():
    """使用跟目录相关的函数"""
    print(os.listdir('dir'))  # 目录列表
    os.mkdir('dir2')  # 创建目录
    os.rmdir('dir2')  # 删除目录
    print(os.getcwd())  # 获取当前工作目录
    os.chdir('dir')  # 修改工作目录
    print(os.getcwd())
    os.mkdir('dir3')  # 修改目录后创建的会在新的目录下
    print(os.path.isdir('dir3'))  # 判断是否是文件夹


if __name__ == '__main__':
    use_dir()
