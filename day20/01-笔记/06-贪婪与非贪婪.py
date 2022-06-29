# 作者: Michael(phb)
# 2022年06月22日23时33分01秒
import re

# 在+号，*号后面加？号，就是非贪婪
s = "This is a number 234-235-22-423"
ret = re.match(r'.+(\d+-\d+-\d+-\d+)', s)
print(ret.group(1))
ret = re.match(r'.+?(\d+-\d+-\d+-\d+)', s)
print(ret.group(1))

print('-'*50)

print(re.match(r"aa(\d+)", "aa2343ddd").group(1))

print(re.match(r"aa(\d+?)", "aa2343ddd").group(1))

print(re.match(r"aa(\d+)ddd", "aa2343ddd").group(1))

print(re.match(r"aa(\d+?)ddd", "aa2343ddd").group(1))
