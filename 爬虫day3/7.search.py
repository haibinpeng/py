# 作者: Michael(phb)
# 2023年03月09日18时16分15秒

import re

pattern = re.compile(r'\d+')

# re.search()，直接查找到符合正则表达式的第一个字符串
m = pattern.search('hello 123456 789')
print(m)

if m:
    print('matching string:', m.group())
    print('position:', m.span())
