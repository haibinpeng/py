# 作者: Michael(phb)
# 2022年06月21日20时38分51秒
G = (x*2 for x in range(5))
# print(G)  # G是一个生成器
# for i in G:
#     print(i)
print(next(G))