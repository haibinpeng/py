# 从列表 [1,4,7,2,5,8] 索引为3的位置开始，依次插入列表 [‘x’,‘y’,‘z’] 的所有元素
list1 = [1, 4, 7, 2, 5, 8]
list2 = ['x', 'y', 'z']
# j = 3
# for i in list2:
#     list1.insert(j, i)
#     j += 1
# print(list1)
list1[3:3] = list2
print(list1)