# 作者: Michael(phb)
# 2022年06月23日19时50分35秒
import re

str1 = '123 hello python'
ret = re.match(r'[\d]', str1)
print(ret.group())
