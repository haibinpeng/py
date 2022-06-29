# 作者: Michael(phb)
# 2022年06月23日22时54分16秒
import copy

a = [1, 2]
b = a
print(id(a))
print(id(b))
b[0] = 6
print(b)
print(a)
c = copy.copy(a)
print(id(c))
c[0] = 8
print(c)
print(a)

print('-'*50)

d = [11, 22]
e = [33, 44]
f = [d, e]
print(f)
print(id(f))
g = copy.copy(f)
print(g)
print(id(g))
print(g[0] is d)  # True
# g[0][0] = 55
d[0] = 55
print(g)
print(d)  # [55, 22]
print(f)
# h = copy.deepcopy(f)
# print(h)
# print(h[0] is d)  # False
# h[0][0] = 66
# print(h)
# print(d)
# print(f)
