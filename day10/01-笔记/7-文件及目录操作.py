import os
import sys


def use_rename():
    os.rename('file1', 'file1')  # 重命名文件


def use_remove():
    os.remove('file1')  # 删除文件,不能删除文件夹


def use_dir():
    """使用跟目录相关的函数"""
    print(os.listdir('dir'))  # 目录列表
    # os.mkdir('dir2')  # 创建目录
    # os.rmdir('dir2')  # 删除目录
    print(os.getcwd())  # 获取当前工作目录
    os.chdir('dir')  # 修改工作目录
    print(os.getcwd())
    # os.mkdir('dir3')  # 修改目录后创建的会在新的目录下
    print(os.path.isdir('file1'))  # 判断是否是文件夹


def dfs(path_name, width):
    """深度优先遍历"""
    file_names = os.listdir(path_name)
    for i in file_names:
        print(' ' * width + i)  # 先打印文件名
        current_name = path_name + '/' + i  # 拼接路径
        if os.path.isdir(current_name):
            dfs(current_name, width + 4)


def python_argv():
    """给python文件传参数"""
    print(len(sys.argv))  # 参数个数
    print(sys.argv)
    print(sys.argv[1])
    # print(sys.argv[5])  # 没有该参数，报错


if __name__ == '__main__':
    # use_rename()
    # use_remove()
    # use_dir()
    # dfs('dir', 0)
    dfs(sys.argv[1], int(sys.argv[2]))  # 传参
    # python_argv()

