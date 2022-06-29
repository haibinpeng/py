# 作者: Michael(phb)
# 2022年06月23日21时13分58秒
import re

c = """
重点把宝马X6、奥迪R8的宣传资料找出来
宝马X6我们有一辆深海蓝4.4LxDrive50i豪华型刚刚到货
奥迪的话水晶银有现货
"""
ret = re.findall(r'.*[a-zA-Z0-9].*', c)
print(ret)
