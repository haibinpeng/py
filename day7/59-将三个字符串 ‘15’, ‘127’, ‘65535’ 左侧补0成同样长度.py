# 将三个字符串 ‘15’, ‘127’, ‘65535’ 左侧补0成同样长度
str1 = ['15', '127', '65535']
length = max([len(i) for i in str1])
for i in str1:
    print(i.rjust(length, '0'))
