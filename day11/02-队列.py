# 作者: Michael(phb)
# 2022年06月10日21时08分41秒
import collections


def use_deque():
    """双端队列"""
    queue = collections.deque(['Eric', 'John', 'Michael'])
    queue.append('luke')  # 增
    print(queue)
    print(queue.popleft())  # 删除左边第一个，删除右边就是pop
    print(queue)
    queue[0] = 'xiongda'
    print(queue)


class CircleQueue:
    """循环队列"""

    def __init__(self, max_size):
        self.max_size = max_size
        self.arr = [0] * max_size
        self.front = 0
        self.rear = 0

    def enqueue(self, element):
        """入队"""
        # 判断是否队满
        # 队满不能入队
        if (self.rear + 1) % self.max_size == self.front:
            print('队列已满')
            return False
        # 队未满，可以入队
        self.arr[self.rear] = element
        self.rear = (self.rear + 1) % self.max_size
        return True

    def dequeue(self):
        # 判断是否队空
        # 队空不能出队
        if self.rear == self.front:
            print('队列为空')
            return False
        element = self.arr[self.front]
        self.front = (self.front + 1) % self.max_size
        return element


if __name__ == '__main__':
    # use_deque()
    que = CircleQueue(5)
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    que.enqueue(4)
    que.enqueue(5)
    print(que.dequeue())
