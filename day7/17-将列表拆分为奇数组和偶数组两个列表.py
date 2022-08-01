# 将列表 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 拆分为奇数组和偶数组两个列表
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = []
for i in list1:
    if i % 2 == 0:
        list2.append(i)
        list1.remove(i)
print(list1)
print(list2)