# 将列表 [3,0,8,5,7] 中大于5元素置为1，其余元素置为0
list1 = [3, 0, 8, 5, 7]
for i in range(len(list1)):
    if list1[i] > 5:
        list1[i] = 1
    else:
        list1[i] = 0
print(list1)
