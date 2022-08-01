# 作者: Michael(phb)
# 2022年06月28日20时28分00秒
from pymysql import *


def main():
    # 创建connection连接
    conn = connect(host='192.168.221.128', user='root', password='peng1997601', database='python6', charset='utf8')
    # 获得cursor对象
    cs1 = conn.cursor()
    # 插入
    # count = cs1.execute("insert into goods_cates(name) values('硬盘')")
    # 修改
    # count = cs1.execute("update goods_cates set name='机械硬盘' where name='硬盘'")
    # 删除
    count = cs1.execute("delete from goods_cates where name='机械硬盘'")
    print(count)
    conn.commit()
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()
