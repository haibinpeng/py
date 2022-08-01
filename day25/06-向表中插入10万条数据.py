# 作者: Michael(phb)
# 2022年06月28日21时16分30秒
from pymysql import connect


def main():
    # 创建connection连接
    conn = connect(host='192.168.221.128', user='root', password='peng1997601', database='python6', charset='utf8')
    # 获得cursor对象
    cs1 = conn.cursor()
    # 插入10万条数据
    for i in range(100000):
        cs1.execute("insert into text_index values('ha-%d')" % i)
    # 提交数据
    conn.commit()
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()
