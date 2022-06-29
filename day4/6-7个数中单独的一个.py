# 有7个整数，其中有6个数出现了两次，1个数出现了一次， 找出出现了一次的那个数
# 任何一个数和自己异或是零，和零异或是自身
list1 = [1, 2, 3, 4, 1, 2, 4]
result = 0
for i in list1:
    result ^= i
print(result)