# 作者: Michael(phb)
# 2022年06月13日20时34分37秒
def bitmap(arr):
    """位图"""
    init_bitmap = 0
    result = []
    for i in arr:
        if not init_bitmap & 1 << i:  # (init_bitmap & 1 << i) == 0表示这个数没出现过
            result.append(i)  # 将这个数放入result
            init_bitmap |= 1 << i  # 把对应位置标记为1
    return result


if __name__ == '__main__':
    list1 = [95, 17, 3, 31, 86, 75, 56, 19, 38, 26,
             94, 54, 53, 72, 59, 61, 74, 58, 78, 60,
             64, 43, 52, 90, 84, 19, 92, 2, 71, 12,
             67, 10, 53, 85, 98, 24, 11, 41, 44, 55,
             10, 47, 43, 98, 9, 55, 18, 30, 44, 22,
             48, 15, 87, 28, 47, 18, 92, 3, 38, 87,
             59, 84, 76, 65, 82, 26, 47, 52, 58, 79,
             50, 82, 5, 71, 28, 30, 17, 51, 11, 58,
             12, 54, 49, 73, 24, 46, 99, 94, 93, 70,
             12, 33, 19, 67, 62, 74, 61, 89, 91, 51]
    result = bitmap(list1)
    result.sort()  # 排序，方便验证
    print(result)
    print(len(result))
    print('*' * 50)
    print(set(list1))
    print(len(set(list1)))
