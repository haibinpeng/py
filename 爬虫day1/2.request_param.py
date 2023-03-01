# 作者: Michael(phb)
# 2023年02月28日22时54分24秒

import requests

kw = {'wd': '长城'}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# params接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get("http://www.baidu.com/s?", params=kw, headers=headers)  # 注意这里的s?

print(response.status_code)
print(response.content.decode())
