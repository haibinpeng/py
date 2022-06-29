# 创建一个空集合，增加 {'x’,'y’,'z’} 三个元素
s1 = {'x', 'y', 'z'}
s2 = set()
s3 = s1.union(s2)
print(s3)
