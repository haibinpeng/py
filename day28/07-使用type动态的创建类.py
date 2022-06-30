# 作者: Michael(phb)
# 2022年06月30日21时57分18秒
# type（类名，由父类名称组成的元组（针对继承的情况，可以为空），包含属性的字典（名称和值））
Test2 = type('Test', (), {})
print(Test2)
print(help(Test2))

print('-' * 50)

# 使用type创建带有属性的类
Foo = type('Foo', (), {'bar': True})
print(Foo.bar)
f = Foo()
print(f)

print('-' * 50)


# 使用type创建带有方法的类
def echo_bar(self):
    print(self.bar)


FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})  # FooChild继承了父类Foo
print(hasattr(Foo, 'echo_bar'))
print(hasattr(FooChild, 'echo_bar'))
f = FooChild()
f.echo_bar()

print('-' * 50)


@staticmethod
def test_static():
    print('static method')


@classmethod
def test_class(cls):
    print(cls.bar)


FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar, 'test_static': test_static, 'test_class': test_class})
f = FooChild()
f.test_static()
f.test_class()
