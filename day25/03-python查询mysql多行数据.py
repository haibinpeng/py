# 作者: Michael(phb)
# 2022年06月28日20时57分34秒
from pymysql import *


def main():
    # 创建connection连接
    conn = connect(host='192.168.221.128', user='root', password='peng1997601', database='python6', charset='utf8')
    # 获得cursor对象
    cs1 = conn.cursor()
    # 执行select语句，返回值是查出的数据总条数
    count = cs1.execute('select * from students where id <5')
    # 打印受影响的行数
    print("查询到%d条数据:" % count)
    # good = cs1.fetchmany(2)
    good = cs1.fetchall()
    print(good)

    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()
