# 作者: Michael(phb)
# 2022年06月30日22时41分27秒
def upper_attr(class_name, class_parents, class_attr: dict):
    # 遍历属性字典，把不是__开头的属性名字变为大写
    new_attr = {}
    for name, value in class_attr.items():
        if not name.startswith('__'):
            new_attr[name.upper()] = value
    return type(class_name, class_parents, new_attr)


class Foo(object, metaclass=upper_attr):  # object是基类，可以省略
    bar = True


# print(Foo.bar)  # 修改后没有此方法了，报错
print(Foo.BAR)
