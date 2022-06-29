# 将字符串 ‘2.72, 5, 7, 3.14’ 以半角逗号切片后，再将各个元素转成浮点型或整形
str1 = '2.72, 5, 7, 3.14'
str2 = str1.split(',')
conv = lambda x: float(x) if '.' in x else int(x)
print(list(map(conv, str2)))
