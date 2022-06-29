# 作者: Michael(phb)
# 2022年06月19日19时45分04秒
from multiprocessing import Process


def run_proc(name, **kwargs):
    print('子进程，修改前'+name)
    print(kwargs)
    name = 'Mike'
    print('子进程，修改后' + name)


if __name__ == '__main__':
    name = 'Michael'
    p = Process(target=run_proc, args=(name,), kwargs={'yf': 22})
    p.start()
    p.join()
    print('父进程，子进程执行后' + name)
