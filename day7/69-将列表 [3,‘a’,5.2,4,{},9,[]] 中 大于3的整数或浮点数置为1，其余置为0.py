# 将列表 [3,‘a’,5.2,4,{},9,[]] 中 大于3的整数或浮点数置为1，其余置为0
list1 = [3, 'a', 5.2, 4, {}, 9, []]


def modify(a):
    if isinstance(a, int):
        return 1 if int(a) > 3 else 0
    elif isinstance(a, float):
        return 1 if float(a) > 3 else 0
    else:
        return 0


list1 = list(map(modify, list1))  # map(func, lst),将传⼊的函数变量func作⽤到lst变量的每个元素中
print(list1)
