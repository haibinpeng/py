# 作者: Michael(phb)
# 2022年06月28日21时11分37秒
from pymysql import *


def main():
    # 创建connection连接
    conn = connect(host='192.168.221.128', user='root', password='peng1997601', database='python6', charset='utf8')
    # 获得cursor对象
    cs1 = conn.cursor()
    # 构造参数列表
    id = ['1 or 1']
    cs1.execute('select * from students where id=%s', id)
    s = cs1.fetchall()
    print(s)
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()
