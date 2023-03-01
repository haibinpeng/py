# 作者: Michael(phb)
# 2023年02月28日23时00分42秒

import requests

response = requests.get("http://www.sina.com.cn")

print(response.request.headers)
print(response.content.decode())
