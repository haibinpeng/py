# 作者: Michael(phb)
# 2022年06月28日21时02分15秒
from pymysql import *


def main():
    # 创建connection连接
    conn = connect(host='192.168.221.128', user='root', password='peng1997601', database='python6', charset='utf8')
    # 获得cursor对象
    cs1 = conn.cursor()
    id = '1 or 1'  # 会造成sql注入
    sql = 'select * from students where id={}'.format(id)
    print(sql)
    cs1.execute(sql)
    s = cs1.fetchall()
    print(s)
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()
