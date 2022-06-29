# 将等长的键列表和值列表转为字典
a = ('A', 'B', 'C', 'D', 'E')
b = (0, 0, 0, 0, 0)
dict1 = dict(zip(a, b))
print(dict1)
