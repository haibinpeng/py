# 作者: Michael(phb)
# 2022年06月22日22时40分03秒
import re

ret = re.findall(r'\d+', "python = 9999, c = 7890, c++ = 12345")
print(type(ret))
print(ret)  # ret是列表，没有group方法
