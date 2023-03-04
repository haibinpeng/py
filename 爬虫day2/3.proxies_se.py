# 作者: Michael(phb)
# 2023年03月02日15时05分48秒

import urllib.request  # Python3将urllib和urllib2合二为一，并重组了下包结构
import socket
import requests
import ssl

mimvp_url = "https://www.baidu.com"

# 全局取消ssl证书验证，防止打开未验证的https网址抛出异常urllib.error.URLError:
ssl._create_default_https_context = ssl._create_unverified_context


# 通过API提供米扑代理,重点
def spider_proxy():
    proxy_url = 'https://proxyapi.mimvp.com/api/fetchopen.php?orderid=863101100211050025&num=100&http_type=1&anonymous=3,5'  # 已过期
    req = urllib.request.Request(proxy_url)
    content = urllib.request.urlopen(req, timeout=30).read()
    proxy = []
    proxy_list = content.decode().split("\r\n")  # 通过'\r\n'分割
    for i in proxy_list:
        proxy.append(i)
    return proxy


proxy_http = {"http": "http://"}
proxy_https = {"https": "http://"}


def test_http(proxy, mimvp_url):
    # 测试代理，urllib
    socket.setdefaulttimeout(60)
    handler = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(handler)
    urllib.request.install_opener(opener)
    content = urllib.request.urlopen(mimvp_url, timeout=60).read().decode("utf8")
    print(len(content), content)
    opener.close()


def test_http_requests(proxy, mimvp_url):
    # 测试代理，requests
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    }

    r = requests.get("https://www.baidu.com", proxies=proxy, headers=headers)
    print(r.status_code)  # 状态码


if __name__ == "__main__":
    ip = spider_proxy()  # 通过API获取米扑代理
    print(ip)
    for i in ip:
        proxy_http["http"] += i  # 拼接，http:i
        # print(proxy_http["http"])
        test_http_requests(proxy_http, mimvp_url)  # http
