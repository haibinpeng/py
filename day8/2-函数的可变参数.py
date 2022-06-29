# def demo(num, num_list):
#     num = 10  # 使用赋值语句
#     num_list = [1, 2, 3]  # 使用赋值语句
#     print(num)
#     print(num_list)
#
#
# num1 = 5
# list1 = [4, 5, 6]
# demo(num1, list1)
# print(num1)  # 没有改变
# print(list1)  # 没有改变

def demo(list1: list, dict1: dict):
    list1.append(4)  # 使用方法修改数据的内容
    dict1['age'] = 18  # 使用方法修改数据的内容
    print(list1)
    print(dict1)


list2 = [1, 2, 3]
dict2 = {'name': 'yf'}
demo(list2, dict2)
print(list2)  # 发生改变
print(dict2)  # 发生改变
