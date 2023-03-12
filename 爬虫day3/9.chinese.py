# 作者: Michael(phb)
# 2023年03月12日17时32分35秒

import re

title = '你好，hello，世界'

# \u4e00-\u9fa5代表汉字范围
pattern = re.compile(r'[\u4e00-\u9fa5]+')

result = pattern.findall(title)
print(result)
