# 删除列表中索引号为奇数（或偶数）的元素
"""
错误的写法，删除一个数据后列表会改变
list1 = [0, 1, 2, 3, 4, 5, 6, 7]
for i in range(len(list1)):
    if i % 2 == 0:
        del list1[i]
print(list1)
"""
list1 = [0, 1, 2, 3, 4, 5, 6, 7]
# del list1[::2]  # 删除索引为偶数的
del list1[1::2]  # 删除索引为奇数的
print(list1)
