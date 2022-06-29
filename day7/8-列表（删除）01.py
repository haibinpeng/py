# 从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除元素‘x’
list1 = [True, 1, 0, 'x', None, 'x', False, 2, True]
list1.pop(3)  # 删除指定索引位置的数据，未指定时删除最后一个元素
list1.remove('x')  # 删除第一个出现的指定数据
print(list1)
