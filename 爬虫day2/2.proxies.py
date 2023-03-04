# 作者: Michael(phb)
# 2023年03月02日14时56分05秒

import requests

proxies = {"http": "http://223.165.1.170:60148"}  # 代理
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}

r = requests.get("https://www.baidu.com", proxies=proxies, headers=headers)
print(r.status_code)
print(r.content.decode())
