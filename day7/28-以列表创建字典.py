# 以列表 [‘A’,‘B’,‘C’,‘D’,‘E’,‘F’,‘G’,‘H’] 中的每一个元素为键，默认值都是0，创建一个字典
# list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# dict1 = {}
# for i in list1:
#     dict1[i] = 0
# print(dict1)
print({}.fromkeys('A B C D E F G H'.split(), 0))
