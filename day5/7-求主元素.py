# 给定一个n个整型元素的列表，其中有一个元素出现次数超过n/2，求这个元素
def find_main(list1):
    count = 1
    main_num = list1[0]
    i = 1
    while i < len(list1):
        if count == 0:
            main_num = list1[i]
            count = 1
            i += 1
        else:
            if main_num == list1[i]:
                count += 1
                i += 1
            else:
                count -= 1
                i += 1
    print(main_num)


list2 = [1, 2, 2, 2, 3, 4, 4, 4, 4, 4, 4]
find_main(list2)
