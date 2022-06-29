# 作者: Michael(phb)
# 2022年06月21日23时18分34秒
import re

email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]

for email in email_list:
    ret = re.match('[\w]{4,20}@163.com$', email)
    if ret:
        print("%s 是符合规定的邮件地址,匹配后的结果是:%s" % (email, ret.group()))
    else:
        print("%s 不符合要求" % email)

list1 = ['bat', 'bit', 'but', 'hat', 'hit', 'hut']
for word in list1:
    ret = re.match('[bh][aiu]t', word)
    if ret:
        print(ret.group())
