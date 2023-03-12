# 作者: Michael(phb)
# 2023年03月09日17时55分40秒

import re

# re模块提供一个方法compile模块，提供我们输入一个匹配的规则，然后返回一个pattern实例，然后我们可以根据这个规则去匹配字符串
pattern = re.compile(r'\d+')

result1 = pattern.findall('hello 123456 789')
print(result1)

result2 = pattern.findall('one1two2three3four4', 0, 10)  # 位置0-10
print(result2)


pattern = re.compile(r'\d+.\d*')

# 通过pattern.findall()方法就能够全部匹配到我们得到的字符串
result = pattern.findall("123.141593, 'bigcat', 232312, 3.15")
# findall以列表形式返回全部能匹配的子串给result
for i in result:
    print(i)
