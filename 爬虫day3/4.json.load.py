# 作者: Michael(phb)
# 2023年03月07日22时41分27秒

# json.load()读取文件中json形式的字符串元素转化为Python类型
# 而json.loads()需要自己read

import json

strList = json.load(open('listStr.json'))
print(strList)
# print(type(strList))  # list

strDict = json.load(open('dictStr.json'))
print(strDict)  # dict
