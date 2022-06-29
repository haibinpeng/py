# 作者: Michael(phb)
# 2022年06月10日23时42分38秒
import random


class MySort:
    def __init__(self, n, num_range):
        self.n = n  # 元素个数
        self.num_range = num_range  # 生成用来排序的随机数的范围
        self.arr = [random.randint(0, num_range) for i in range(n)]  # 随机生成0-num_range的数放入列表，进行排序

    def bubble(self):
        """冒泡排序"""
        i = self.n - 1
        arr = self.arr
        while i > 0:
            j = 0
            while j < i:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j += 1
            i -= 1

    def select(self):
        """选择排序"""
        i = 0
        arr = self.arr
        while i < self.n - 1:
            min_pos = i
            j = i + 1
            while j < self.n:
                if arr[j] < arr[min_pos]:
                    min_pos = j
                j += 1
            arr[i], arr[min_pos] = arr[min_pos], arr[i]
            i += 1

    def insert(self):
        """插入排序"""
        arr = self.arr
        i = 1
        while i < self.n:
            insert_val = arr[i]
            j = i - 1  # 从后往前比
            while j >= 0:
                if insert_val < arr[j]:
                    arr[j + 1] = arr[j]
                else:
                    break
                j -= 1
            arr[j + 1] = insert_val
            i += 1

    def shell(self):
        arr = self.arr
        # 最外层循环控制步长
        gap = self.n >> 1
        while gap > 0:  # 将插入排序，5个为1的地方，改为gap
            i = gap
            while i < self.n:  # i依次拿的每一个无序数
                insert_val = arr[i]
                j = i - gap
                while j >= 0:  # 内层是一个有序序列，要把insert_val放入有序序列
                    if insert_val < arr[j]:
                        arr[j + gap] = arr[j]
                    else:
                        break
                    j -= gap
                arr[j + gap] = insert_val
                i += 1  # 这里不变
            gap = gap >> 1

    def partition(self, left, right):
        """找到分割值的下标"""
        arr = self.arr
        k = left  # k始终指向要放置的比分割值小的元素的位置
        for i in range(left, right):
            if arr[i] < arr[right]:
                arr[k], arr[i] = arr[i], arr[k]
                k += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def quick(self, left, right):
        """快速排序"""
        if left < right:
            pivot = self.partition(left, right)  # pivot是分割值的下标
            self.quick(left, pivot - 1)
            self.quick(pivot + 1, right)

    def adjust_max_heap(self, pos, length):
        """
        调整某个子树为大根堆
        :param pos:调整的子树的根
        :param length:整个堆的元素个数
        :return:
        """
        arr = self.arr
        dad = pos
        son = 2 * dad + 1
        while son < length:
            if son + 1 < length and arr[son] < arr[son + 1]:
                son += 1
            if arr[son] > arr[dad]:
                arr[son], arr[dad] = arr[dad], arr[son]
                dad = son
                son = 2 * dad + 1
            else:
                break

    def heap(self):
        """堆排序"""
        arr = self.arr
        for i in range(self.n // 2 - 1, -1, -1):
            self.adjust_max_heap(i, self.n)
        arr[0], arr[self.n - 1] = arr[self.n - 1], arr[0]  # 交换顶部元素和最后一个元素
        for i in range(self.n - 1, 1, -1):  # 把剩余元素调整为大根堆
            self.adjust_max_heap(0, i)
            arr[0], arr[i - 1] = arr[i - 1], arr[0]

    def test_sort(self, sort_method, *args, **kwargs):
        print(self.arr)
        sort_method(*args, **kwargs)
        print(self.arr)


if __name__ == '__main__':
    s = MySort(10, 99)
    # s.test_sort(s.bubble)
    # s.test_sort(s.select)
    # s.test_sort(s.insert)
    # s.test_sort(s.shell)
    # s.test_sort(s.quick, 0, s.n - 1)
    s.test_sort(s.heap)
