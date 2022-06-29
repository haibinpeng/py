age = 18
name = 'Michael'
weight = 55.5
num = 1

# 我今年的年龄是x岁
print('我今年的年龄是%d岁' % age)

# 我的名字是x
print('我的名字是%s' % name)

# 我的体重是x公斤
print('我的体重是%.2f公斤' % weight)

# 我的学号是x
print('我的学号是%d' % num)

# 我的学号是001
print('我的学号是%03d' % num)

# 我的名字是x，明年x+1岁了
print('我的名字是%s，明年%d岁了' % (name, age+1))
print('我的名字是%s，明年%s岁了' % (name, age+1))
print(f'我的名字是{name}，明年{age + 1}岁了')

# 我的名字是x，今年x岁了，我的体重是x公斤，我的学号是x
print('我的名字是%s，今年%d岁了，我的体重是%.2f公斤，我的学号是%06d' % (name, age, weight, num))