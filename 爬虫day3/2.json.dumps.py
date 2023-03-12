# 作者: Michael(phb)
# 2023年03月07日22时25分00秒

import json

listStr = [1, 2, 3, 4]  # list
tupleStr = (1, 2, 3, 4)  # tuple
dictStr = {"city": "北京", "name": "大猫"}

print(json.dumps(listStr))
print(type(json.dumps(listStr)))  # str  '[1, 2, 3, 4]'

print(json.dumps(tupleStr))  # str  '[1, 2, 3, 4]'

# json.dumps()序列化时默认使用的ascii编码
# 添加参数ensure_ascii-False禁用ascii编码，按utf-8编码

print(json.dumps(dictStr))  # '{"city": "\u5317\u4eac", "name": "\u5927\u732b"}'
print(json.dumps(dictStr, ensure_ascii=False))  # str  '{"city": "北京", "name": "大猫"}'
