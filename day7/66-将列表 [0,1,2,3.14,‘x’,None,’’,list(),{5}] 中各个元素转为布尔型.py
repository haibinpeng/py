# 将列表 [0,1,2,3.14,‘x’,None,’’,list(),{5}] 中各个元素转为布尔型
list1 = [0, 1, 2, 3.14, 'x', None, '', list(), {5}]
a = [bool(x) for x in list1]
print(a)
