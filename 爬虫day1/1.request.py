# 作者: Michael(phb)
# 2023年02月28日22时03分57秒

import requests

# 要带header，不然很容易被判断出来为爬虫
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

response = requests.get('https://www.baidu.com/', headers=headers)

# print(response.text)

# 查看响应内容，response.content返回的字节流数据
print(response.content.decode())

# # 查看完整url地址
# print(response.url)
#
# # 查看响应头部字符编码
# print(response.encoding)
#
# # 查看响应码
# print(response.status_code)
# print(response.headers)
#
# print(response.request.headers)
