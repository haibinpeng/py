# 将三个全英文字符串（比如，‘ok’, ‘hello’, ‘thank you’）分行打印，实现左对齐、右对齐和居中对齐效果
str1 = ['ok', 'hello', 'thank you']
for i in str1:
    print(i.ljust(10))
for i in str1:
    print(i.rjust(10))
for i in str1:
    print(i.center(10))
