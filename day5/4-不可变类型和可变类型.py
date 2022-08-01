# 不可变类型
# def modify(num):
#     num = 5
#
#
# a = 10
# print('before', a, id(a))
# modify(a)
# print('late', a, id(a))


# 可变类型
def modify(list2):
    list2.append(3)

list1 = [1, 2]
print('before', list1, id(list1))
modify(list1)
print('late', list1, id(list1))