# 作者: Michael(phb)
# 2022年07月04日09时21分52秒
import requests

response = requests.get("http://www.sina.com")
print(response.request.headers)
print(response.content.decode())
