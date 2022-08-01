# 作者: Michael(phb)
# 2022年06月21日21时02分38秒
def gen():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i += 1


G = gen()
print(next(G))
print(G.send(None))
print(G.send('a'))
print(next(G))
print(G.__next__())
# print(G.__next__())
