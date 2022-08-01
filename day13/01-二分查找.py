# 作者: Michael(phb)
# 2022年06月13日20时19分00秒
def bsearch(arr, target):
    """二分查找"""
    high = len(arr) - 1
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if target < arr[mid]:
            high = mid - 1
        elif target > arr[mid]:
            low = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    list1 = [1, 3, 9, 13, 27, 41, 42, 71, 71, 83, 98, 100]
    print(bsearch(list1, 98))
