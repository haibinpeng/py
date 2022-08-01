# 向字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中追加 ‘David’:19 键值对，更新Cecil的值为17
dict1 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
# 如果 key 不存在，会新增键值对
dict1["David"] = 19
# 如果 key 存在，会修改已经存在的键值对
dict1["Cecil"] = 17
print(dict1)
