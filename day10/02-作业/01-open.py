import os

file = open('test', 'w+', encoding='utf8')
file.write('人生苦短，我用python')
file.seek(0, os.SEEK_SET)
txt = file.read()
print(txt)
file.close()
