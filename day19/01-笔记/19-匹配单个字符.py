# 作者: Michael(phb)
# 2022年06月21日22时51分25秒
import re

# .：匹配任意1个字符，除了\n
ret = re.match(".", "M")
print(ret.group())

ret = re.match("t.o", "too")
print(ret.group())

ret = re.match("t.o", "two")
print(ret.group())

print('-' * 50)

# []：匹配[]中列举的字符
# 大小写h都可以的情况
ret = re.match("[hH]", "hello Python")
print(ret.group())

ret = re.match("[hH]", "Hello Python")
print(ret.group())

ret = re.match("[hH]ello Python", "Hello Python")
print(ret.group())

# 匹配0到9第一种写法
ret = re.match("[0123456789]Hello Python", "7Hello Python")
print(ret.group())

# 匹配0到9第二种写法
ret = re.match("[0-9]Hello Python", "7Hello Python")
print(ret.group())

ret = re.match("[0-35-9]Hello Python", "7Hello Python")
print(ret.group())

# 下面这个正则不能够匹配到数字4，因此ret为None
ret = re.match("[0-35-9]Hello Python", "4Hello Python")
if ret:
    print(ret.group())

print('-' * 50)

# \d：匹配数字
ret = re.match("嫦娥\d号", "嫦娥1号发射成功")
print(ret.group())

ret = re.match("嫦娥\d号", "嫦娥2号发射成功")
print(ret.group())

ret = re.match("嫦娥\d号", "嫦娥3号发射成功")
print(ret.group())

print('-' * 50)

# \s：匹配空白
ret = re.match("嫦娥\s号", "嫦娥 号发射成功")
print(ret.group())

print('-' * 50)

# \w：匹配单词字符
ret = re.match("张\w", '张三爱学python')
print(ret.group())
