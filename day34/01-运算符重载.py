# 作者: Michael(phb)
# 2022年07月07日20时11分03秒
class Person:
    def __init__(self, age):
        self.age = age

    def __gt__(self, other):
        return self.age > other.age


bob = Person(18)
andy = Person(16)
print(bob > andy)
