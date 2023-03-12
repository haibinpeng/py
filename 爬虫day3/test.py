# 作者: Michael(phb)
# 2023年03月12日17时46分34秒
import re
print(re.findall(r"<a class=\"article-item-title weight-bold\".*?>(.*?)</a>",
                 """'<a class="article-item-title weight-bold" href="/p/2168252921032964" target="_blank" sensors_operation_list="page_flow">陪伴了创投40年的硅谷银行，却不敌市场情绪的40个小时</a>"""))