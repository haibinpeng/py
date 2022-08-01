# 将二维列表 [[1], [‘a’,‘b’], [2.3, 4.5, 6.7]] 转为一维列表
list1 = [[1], ['a', 'b'], [2.3, 4.5, 6.7]]
list2 = [j for i in list1 for j in i]
print(list2)
