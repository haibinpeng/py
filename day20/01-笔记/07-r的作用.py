# 作者: Michael(phb)
# 2022年06月22日23时41分16秒
import re

mm = "c:\\a\\b\\c"
print(len(mm))
print(mm)

# r的作用就是让\默认经过了一次转义
print(re.match(r"c:\\", mm).group())

# r不对其他正则做转义，只对\
print(re.match(r'.bc', 'abc').group())
