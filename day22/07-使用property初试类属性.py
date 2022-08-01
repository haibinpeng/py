# 作者: 王道 龙哥
# 2022年06月23日10时51分04秒
class Foo:

    def get_bar(self):
        return 'laowang'

    def set_bar(self, value):
        print(value)

    def del_bar(self):
        print('del_bar')

    Bar = property(get_bar, set_bar, del_bar, 'I am Bar 的注释')


obj = Foo()
print(obj.Bar)  # 第一个参数是方法名，调用对象.属性时自动触发执行方法
obj.Bar = 200  # 第二个参数是方法名，调用对象.属性=XXX时自动触发执行方法
del obj.Bar  # 第三个参数是方法名，调用del对象.属性时自动触发执行方法
print(Foo.Bar.__doc__)  # 第四个参数是字符串，调用对象.属性_doc_，此参数是该属性的描述
