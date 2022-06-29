# 作者: Michael(phb)
# 2022年06月23日21时46分51秒
import re

e = """
这是小明的邮箱：xiaoming@163.com
这是小美的邮箱：xiaomei@126.com
这是小刚的邮箱：xiaogang@gmail.com
"""

ret = re.sub(r'[a-zA-Z0-9]{4,20}@(163|126|gmail)\.com', r'my_email@qq.com', e)
print(ret)
