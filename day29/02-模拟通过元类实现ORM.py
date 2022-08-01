# 作者: Michael(phb)
# 2022年07月01日20时14分20秒
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs: dict):
        mappings = {}
        for k, v in attrs.items():
            if isinstance(v, tuple):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        # 删除已经在字典中存储的属性
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class User(metaclass=ModelMetaclass):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def save(self):
        fields = []  # fields里边放表的字段名
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v[0])  # v是元组
            args.append(getattr(self, k, None))
        sql = f"""insert into {self.__table__} ({",".join(fields)}) values ({",".join(["'"+i+"'" if isinstance(i,str) else str(i) for i in args])})"""
        print(sql)


u = User(uid=12345, name='Michael', email='test@orm.org', password='my-pwd')
print(u.__dict__)
u.save()
