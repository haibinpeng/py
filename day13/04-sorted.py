# 作者: Michael(phb)
# 2022年06月13日21时21分09秒
list1 = [5, 2, 3, 1, 4]
print(sorted(list1))
print(list1)  # sorted函数不会改变原有的list，而是返回一个新的排好序的list
list1.sort()
print(list1)  # list.sort()改变原list的内容

print('-' * 50)

print(sorted("This is a test string from Andrew".split()))
print(sorted("This is a test string from Andrew".split(), key=str.lower))

print('-' * 50)

student_tuples = [
    ('jone', 'B', 12),
    ('dave', 'B', 10),
    ('john', 'A', 15),
]


def youming(student):
    return student[1]


# lambda是匿名函数,匿名函数只能用一次，而且逻辑简单
# s就是形参，等价于youming里的student，s[1]就是返回值，等价于student[1]
print(sorted(student_tuples, key=youming))
print(sorted(student_tuples, key=lambda s: s[1]))

print('-' * 50)
print('排序列表内是自定义对象')


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        """
        str必须返回的是字符串类型，repr和str功能一样，只是可以返回的类型不是字符串
        :return:
        """
        return repr((self.name, self.grade, self.age))


s = Student('john', 'A', 15)
print(s)
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print(sorted(student_objects, key=lambda s: s.age))

print('-' * 50)
print('operator的使用')

from operator import itemgetter, attrgetter

print(sorted(student_tuples, key=itemgetter(2)))
print(sorted(student_objects, key=attrgetter('age')))

print('-' * 50)
print('同时还支持多层排序')

print(sorted(student_tuples, key=itemgetter(1, 2)))
print(sorted(student_objects, key=attrgetter('grade', 'age')))

print('-' * 50)
print('降序')

print(sorted(student_tuples, key=itemgetter(2), reverse=True))
print(sorted(student_objects, key=attrgetter('age'), reverse=True))

print('-' * 50)
print('稳定性')

data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print(sorted(data, key=lambda s: s[0]))

print('-' * 50)
print('字典中混合列表排序')

mydict = {'Li': ['M', 7],
          'Zhang': ['E', 2],
          'Wang': ['P', 3],
          'Du': ['C', 2],
          'Ma': ['C', 9],
          'Zhe': ['H', 7]}

print(sorted(mydict.items(), key=lambda v: v[0]))
# 针对字典mydict的value结构[n,m]中的m按照从小到大的顺序排列
print(sorted(mydict.items(), key=lambda v: v[1][1]))

print('-' * 50)
print('列表中嵌入字典排序')

gameresult = [
    {"name": "Bob", "wins": 10, "losses": 3, "rating": 75.00},
    {"name": "David", "wins": 3, "losses": 5, "rating": 57.00},
    {"name": "Carol", "wins": 4, "losses": 5, "rating": 57.00},
    {"name": "Patty", "wins": 9, "losses": 3, "rating": 71.48}]

print(sorted(gameresult, key=itemgetter('rating', 'name')))  # 注意这里不是attrgetter()
