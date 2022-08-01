# 作者: Michael(phb)
# 2022年06月22日22时42分08秒
import re

ret = re.sub(r'\d+', '998', 'python 997')
print(type(ret))
print(ret)

print('-' * 50)


def add(temp):
    # print(temp)
    str_num = temp.group()
    num = int(str_num) + 5
    return str(num)


ret = re.sub(r'\d+', add, 'python 992')
print(ret)

print('-' * 50)

ret = re.sub(r'\d+', lambda x: str(int(x.group()) + 5), 'python 992')
print(ret)

print('-' * 50)

s = 'hello world, now is 2020/7/20 18:48, 现在是2020年7月20日18时48分。'
ret = re.sub(r'年|月', r'/', s)
ret = re.sub(r'日', r' ', ret)
ret = re.sub(r'时', r':', ret)
ret = re.sub(r'分', r'', ret)
print(ret)

print('-' * 50)

# 字符串很长，里边有单引号，和双引号，可以使用三引号
import re

test_str = '''
<div>
        <p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

        </div>
'''
ret = re.sub(r'<\w+>|</\w+>|&nbsp;', r'', test_str)
# ret = re.sub(r'<[^>]*>|&nbsp;|\n', r'', test_str)
print(ret)
