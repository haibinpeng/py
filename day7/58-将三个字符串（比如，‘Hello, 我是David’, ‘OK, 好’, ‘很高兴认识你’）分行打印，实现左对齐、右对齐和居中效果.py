# 将三个字符串（比如，‘Hello, 我是David’, ‘OK, 好’, ‘很高兴认识你’）分行打印，实现左对齐、右对齐和居中效果
str1 = ['Hello,我是David', 'OK,好', '很高兴认识你']
for i in str1:
    print(i.ljust(20))
for i in str1:
    print(i.rjust(20))
for i in str1:
    print(i.center(20))
