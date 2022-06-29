import os

f = open('Readme', encoding='utf8')
# f.seek(5, os.SEEK_SET)  # utf-8一个汉字是三个字节，汉字偏移时不是3的整数倍会报错
f.seek(6, os.SEEK_SET)
txt = f.read()
print(txt)
