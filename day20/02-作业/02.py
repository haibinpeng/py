# 作者: Michael(phb)
# 2022年06月23日00时09分22秒
import re

a = ['http://www.yahoo.com', 'http://www.baiducom',
     'http://www.yf.net', 'http://www.csu.edu.cn', 'http://www.csu.edu.cn1']
for i in a:
    ret = re.match(r'.+[w]{3}\..+\.(com|net|edu.cn)$', i)
    if ret:
        print('{}是符合条件的域名'.format(i))
    else:
        print('{}不是符合条件的域名'.format(i))
