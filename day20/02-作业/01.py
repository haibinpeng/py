# 作者: Michael(phb)
# 2022年06月22日23时56分19秒
import re

ret = re.match(r'[a-zA-Z]+[. ][a-zA-Z]+', 'L.smith')
print(ret.group())
ret = re.match(r'[a-zA-Z]+[, ][a-zA-Z]+', 'L smith')
print(ret.group())
