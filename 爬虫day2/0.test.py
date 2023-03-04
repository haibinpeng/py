# 作者: Michael(phb)
# 2023年03月01日22时31分07秒

import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
response = requests.get('https://fanyi.baidu.com/', headers=headers)
print(response.content.decode())
print(re.findall(";window.gtk = (.*?);", response.content.decode()))
