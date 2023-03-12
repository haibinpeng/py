# 作者: Michael(phb)
# 2023年03月06日22时34分12秒

# 理解json.loads，json.loads()把json字符串转化为python类型

import json

strList = '[1, 2, 3, 4]'
strDict = '{"city": "北京", "name": "大猫"}'  # str
print(type(strDict))

print(json.loads(strList))
print(type(json.loads(strList)))  # list

print(json.loads(strDict))
print(type(json.loads(strDict)))  # dict


# 把豆瓣电影的json对象转换为dict类型

# import json
# import parse_url
# from pprint import pprint
#
# url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"
# html_str = parse_url.parse_url(url)
# print(type(html_str))
#
# ret1 = json.loads(html_str)
# pprint(ret1)
# print(type(ret1))
#
# # with open('douban1.json', 'w', encoding='utf-8') as f:
# #     # json.dump()将python内置类型序列转化为json对象后写入文件
# #     json.dump(ret1, f, ensure_ascii=False, indent=2)
#
# # 如果使用json.dumps()，需要write()
# with open('douban2.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(ret1, ensure_ascii=False, indent=2))
