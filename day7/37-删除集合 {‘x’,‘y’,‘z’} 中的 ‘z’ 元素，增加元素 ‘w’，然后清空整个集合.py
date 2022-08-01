# 删除集合 {‘x’,‘y’,‘z’} 中的 ‘z’ 元素，增加元素 ‘w’，然后清空整个集合
s1 = {'x', 'y', 'z'}
s1.remove('z')
print(s1)
s1.add('w')
print(s1)
s1.clear()
print(s1)
