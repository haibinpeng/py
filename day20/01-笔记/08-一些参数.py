# 作者: Michael(phb)
# 2022年06月22日23时51分30秒
import re

ret = re.match(r'a', 'A', re.I)  # 不区分大小写
print(ret.group())

ret = re.match(r'.bc', '\nbc', re.S)  # 让.也匹配\n
print(ret.group())
