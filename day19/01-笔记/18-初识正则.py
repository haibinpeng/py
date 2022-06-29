# 作者: Michael(phb)
# 2022年06月21日22时45分28秒
import re

# 使用match方法进行匹配操作
result = re.match('yf', 'yf1haha')
# 如果上一步匹配到数据的话，可以使用group方法来提取数据
print(result.group())
