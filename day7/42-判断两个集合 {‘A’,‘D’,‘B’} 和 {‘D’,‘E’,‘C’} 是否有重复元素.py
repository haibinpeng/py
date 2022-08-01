# 判断两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 是否有重复元素
s1 = {'A', 'D', 'B'}
s2 = {'D', 'E', 'C'}
# if s1.intersection(s2):
#     print('有重复元素')
# else:
#     print('没有重复元素')
print(s1.isdisjoint(s2))  # 没有返回True
