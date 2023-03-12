# 作者: Michael(phb)
# 2023年03月07日22时57分19秒

import json
import parse_url
from pprint import pprint

url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"

html_str = parse_url.parse_url(url)

# json.loads()

ret1 = json.loads(html_str)
pprint(ret1)
print(type(ret1))

# 如果要先从文件中读取数据，需要自己read
with open('toutiao.json', 'r', encoding='utf-8') as f:
    ret2 = f.read()  # 要先读
    ret3 = json.loads(ret2)
    pprint(ret3)

# json.load()

# 可以直接从文件中读取数据
with open('toutiao.json', 'r', encoding='utf-8') as f:
    ret4 = json.load(f)  # 直接读
    pprint(ret4)

# json.dumps()

with open('douban.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(ret1, ensure_ascii=False, indent=4))  # 需要先write

# json.dump()

with open('douban1.json', 'w', encoding='utf-8') as f:
    json.dump(ret1, f, ensure_ascii=False, indent=4)
