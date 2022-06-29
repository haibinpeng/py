# 作者: Michael(phb)
# 2022年06月26日22时11分35秒
class Province:
    country = '中国'

    def __init__(self, name):
        self.name = name


taiwan = Province('台湾省')
print(Province.country)
print(taiwan.__class__)  # 输出对象所属类
print(type(taiwan))
