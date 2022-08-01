# 返回在元组 (2,5,3,7) 索引号为2的位置插入元素9之后的新元组
tuple1 = (2, 5, 3, 7)
tuple2 = tuple1[:2]+(9,)+tuple1[2:]
print(tuple2)
