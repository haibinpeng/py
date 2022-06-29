import os
import sys


def dfs(path_name, width):
    file_name = os.listdir(path_name)
    for i in file_name:
        print(' '*width + i)
        cur_name = path_name + '/' + i
        if os.path.isdir(cur_name):
            dfs(cur_name, width+4)


if __name__ == '__main__':
    dfs('dir', 0)
    # dfs(sys.argv[1], 0)
