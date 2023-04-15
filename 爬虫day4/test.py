# 作者: Michael(phb)
# 2023年04月10日13时12分20秒

cookies = [{'a': "b", "c": "d", "e":"f"}, {"a": "f", "c": "d"}]
cookies = {i["a"]: i["c"] for i in cookies}
print(cookies)
