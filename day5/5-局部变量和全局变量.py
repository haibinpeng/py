# num = 10  # 全局变量
#
#
# def func():
#     num = 0  # 局部变量
#     # global num  # 引用全局变量
#     # num = 0
#     print('in', num)
#
#
# func()
# print('out', num)

# if里定义的变量是全局变量
if True:
    i = 1
    print(i)
print(i)

# 循环里定义的变量是全局变量
for j in range(0, 2):
    print(j)
print(j)
