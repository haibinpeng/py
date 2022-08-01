# 作者: Michael(phb)
# 2022年06月28日22时38分53秒
def test():
    print('--- test func ---')


test()
ret = test
print(id(test))
print(id(ret))
