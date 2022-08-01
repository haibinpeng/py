# 作者: Michael(phb)
# 2022年06月21日22时39分03秒
from gevent import monkey

monkey.patch_all()
import gevent
import time
import requests


def coroutine_work(url):
    print('GET: %s' % url)
    response = requests.get(url)
    data = response.text
    print('%d bytes received from %s.' % (len(data), url))


start = time.time()
gevent.joinall([
    gevent.spawn(coroutine_work, "http://www.baidu.com/"),
    gevent.spawn(coroutine_work, "http://www.cskaoyan.com/"),
    gevent.spawn(coroutine_work, "http://www.qq.com/")
])
end = time.time()
print(end - start)
