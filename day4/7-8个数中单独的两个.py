list1 = [1, 2, 3, 4, 1, 2, 3, 6]
result, num1, num2 = 0, 0, 0
for i in list1:
    result ^= i
print(result)
num = result & -result  # 得到最低位为1的数，用于分堆
for i in list1:
    if num & i:  # 分成两堆，为真的一堆，为假的一堆，每一堆里有一个未重复的数
        num1 ^= i
    else:
        num2 ^= i
print(f'第一个为{num1},第二个为{num2}')