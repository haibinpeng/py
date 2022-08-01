# 返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 未重复的元素的集合
s1 = {'A', 'D', 'B'}
s2 = {'D', 'E', 'C'}
uni = s1.intersection(s2)  # 交集
print(s1.union(s2).difference(uni))
