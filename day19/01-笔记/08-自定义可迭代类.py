# 作者: Michael(phb)
# 2022年06月20日23时06分43秒
from collections.abc import Iterable, Iterator


class MyList:
    """
    自定义一个容器MyList用来存放数据，可以通过add方法向其中添加数据
    """

    def __init__(self):
        self.container = []

    def add(self, item):
        self.container.append(item)

    def __iter__(self):
        """返回一个迭代器"""
        myiterator = MyIterator(self)
        return myiterator


class MyIterator:
    """
    自定义的供上面可迭代对象使用的一个迭代器
    对迭代器调用iter，返回类型必须是迭代器
    """
    def __init__(self, mylist):
        self.mylist = mylist
        # current用来记录当前访问的位置
        self.current = 0

    def __next__(self):
        if self.current < len(self.mylist.container):
            item = self.mylist.container[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    mylist = MyList()
    # print(next(mylist))  # 'MyList' object is not an iterator
    print(isinstance(mylist, Iterable))
    print(isinstance(mylist, Iterator))
    print(isinstance(iter(mylist), Iterator))
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    for num in mylist:
        print(num)
    myiterator = MyIterator(mylist)
    print(isinstance(myiterator, Iterator))
    print(next(myiterator))
