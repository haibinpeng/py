# 作者: Michael(phb)
# 2023年03月04日11时39分00秒

import requests

response = requests.get('https://www.baidu.com')

# 返回CookieJar对象
cookiejar = response.cookies
print(cookiejar)

# 将CookieJar转为字典
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
print(cookiedict)

# 通过cookiejar_from_dict转换回去
cookiejar2 = requests.utils.cookiejar_from_dict({'BDORZ': '27315'})
print(cookiejar2)
