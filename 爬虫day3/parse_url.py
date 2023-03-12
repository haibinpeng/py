# 作者: Michael(phb)
# 2023年03月06日22时47分58秒

import requests
from retrying import retry  # retrying是一个python的重试包，可以用来自动重试一些可能运行失败的程序段，retrying提供一个装饰器函数retry，被装饰的函数就会在运行失败的情况下重新执行

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}


# 使用retry尝试多次请求
@retry(stop_max_attempt_number=3)  # 装饰器，最多尝试3次
def _parse_url(url, method, data, proxies):
    print("*" * 20)
    if method == "POST":
        response = requests.post(url, data=data, headers=headers, proxies=proxies)
    else:
        response = requests.get(url, headers=headers, timeout=3, proxies=proxies)
    assert response.status_code == 200  # 断言，如果！=200，程序就会直接在这里崩掉，不会再执行下面的return
    return response.content.decode()


def parse_url(url, method="GET", data=None, proxies={}):  # proxies可以使用代理
    try:
        html_str = _parse_url(url, method, data, proxies)
    except:
        html_str = None
    return html_str


if __name__ == '__main__':
    url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"
    print(parse_url(url))
    print(type(parse_url(url)))
