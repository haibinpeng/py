# 作者: Michael(phb)
# 2022年06月21日20时40分50秒
def fib(n):
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num1
        num1, num2 = num2, num1 + num2
        current += 1
        yield num
    return 'done'


F = fib(5)  # F是一个生成器对象
print(type(F))
# for i in F:
#     print(i)
while True:
    try:
        x = next(F)
        print(f'value:{x}')
    except StopIteration as e:
        print(f'生成器返回值:{e.value}')
        break
