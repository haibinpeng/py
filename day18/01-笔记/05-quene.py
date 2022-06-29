# 作者: Michael(phb)
# 2022年06月19日22时17分43秒
from multiprocessing import Queue

q = Queue(3)
q.put('A')
q.put('B')
print(q.full())
q.put('C')
print(q.full())
try:
    # q.put('D')  # 如果block使用默认值，默认为True且没有设置timeout,消息列队如果为空，此时程序将被阻塞（停在读取状态）
    # q.put('D', True, 2)  # 设置了timeout，则会等待timeout秒，还没收到消息就抛异常
    # q.put('D', False)  # 设为False，消息队列为空，立即抛异常
    q.put_nowait('D')
except:
    print(f'消息队列已满，现有消息数量{q.qsize()}')
if not q.full():
    q.put_nowait('D')
if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())
