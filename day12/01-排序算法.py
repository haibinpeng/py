# 作者: Michael(phb)
# 2022年06月12日16时05分14秒
import random
import time


class MySort:
    def __init__(self, n, num_range):
        self.n = n  # 元素个数
        self.num_range = num_range
        self.arr = [random.randint(0, num_range) for i in range(n)]
        self.help_arr = [0] * n  # 归并时用的辅助列表，不在子方法内定义可以避免每次递归重复开辟空间

    def merge_arr(self, low, mid, high):
        help_arr = self.help_arr
        arr = self.arr
        for i in range(low, high + 1):  # 把原列表内的内容复制到辅助列表
            help_arr[i] = arr[i]
        i = low
        j = mid + 1
        k = low
        while i <= mid and j <= high:
            if help_arr[i] < help_arr[j]:
                arr[k] = help_arr[i]
                k += 1
                i += 1
            else:
                arr[k] = help_arr[j]
                k += 1
                j += 1
        while i <= mid:
            arr[k] = help_arr[i]
            k += 1
            i += 1
        while j <= high:
            arr[k] = help_arr[j]
            k += 1
            j += 1

    def merge(self, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge(low, mid)
            self.merge(mid + 1, high)
            self.merge_arr(low, mid, high)

    def count(self):
        arr = self.arr
        count_arr = [0] * (self.num_range + 1)
        for i in arr:
            count_arr[i] += 1
        # 回填
        k = 0
        for i in range(0, self.num_range + 1):
            for j in range(0, count_arr[i]):
                arr[k] = i
                k += 1

    def test_sort(self, sort_method, *args, **kwargs):
        # print(self.arr)
        start = time.time()
        sort_method(*args, **kwargs)
        end = time.time()
        # print(self.arr)
        print(end - start)


if __name__ == '__main__':
    s = MySort(100000, 99)
    # s.test_sort(s.merge, 0, s.n - 1)
    s.test_sort(s.count)
