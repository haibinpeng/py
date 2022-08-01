# 作者: Michael(phb)
# 2022年06月22日22时37分56秒
import re

ret = re.search(r"\d+", "阅读次数为9999")
print(type(ret))
print(ret.group())
