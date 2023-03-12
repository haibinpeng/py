# 作者: Michael(phb)
# 2023年03月07日22时33分14秒

# json.dump()将python内置类型序列化为json对象（str)后写入文件
# 而json.dumps()需要自己write

import json

listStr = [{'city': '北京'}, {'name': '大刘'}]
# print(type(listStr))
json.dump(listStr, open('listStr.json', 'w'), ensure_ascii=False)

dictStr = {'city': '北京', 'name': '大刘'}
json.dump(dictStr, open('dictStr.json', 'w'), ensure_ascii=False)
