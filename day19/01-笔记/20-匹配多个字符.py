# 作者: Michael(phb)
# 2022年06月21日22时56分20秒
import re

# *：匹配前一个字符出现0次或者无限多次
ret = re.match("[A-Z][a-z]*", "MM")
print(ret.group())

ret = re.match("[A-Z][a-z]*", "MnnM")
print(ret.group())

ret = re.match("[A-Z][a-z]*", "Aabcdef")
print(ret.group())

print('-' * 50)

# +：匹配前一个字符出现1次或者无限多次
names = ["name1", "_name", "2_name", "__name__"]
for name in names:
    ret = re.match('[a-zA-Z_]+[\w]*', name)
    if ret:
        print("变量名 %s 符合要求" % ret.group())
    else:
        print("变量名 %s 非法" % name)

print('-' * 50)

# ?：匹配前一个字符出现1次或0次
ret = re.match('[1-9]?[0-9]', '7')
print(ret.group())

ret = re.match('[1-9]?\d', '33')
print(ret.group())

ret = re.match("[1-9]?\d", "09")
print(ret.group())  # \d匹配了0

print('-' * 50)

# {m}：匹配前一个字符出现m次
# {m,n}：匹配前一个字符出现从m到n次
ret = re.match("[a-zA-Z0-9_]{6}", "12a3g45678")
print(ret.group())

ret = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s34455ff66")
print(ret.group())

email = 'yfyf@163.com'
ret = re.match('[a-zA-Z0-9_]{4,20}@163.com', email)
print(ret.group())
