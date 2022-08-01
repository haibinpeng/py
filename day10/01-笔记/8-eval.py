import os


def use_eval():
    """读取配置文件"""
    f = open('network', 'r+', encoding='utf8')
    net_info = eval(f.read())
    print(type(net_info))
    print(net_info)


def not_use_eval():
    """位置字符串有安全风险"""
    # os.system('ls')  # python里嵌套Linux命令
    eval("__import__('os').system('ls')")  # 等价于上一句


if __name__ == '__main__':
    # use_eval()
    not_use_eval()
