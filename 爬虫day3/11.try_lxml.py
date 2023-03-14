# 作者: Michael(phb)
# 2023年03月13日22时09分04秒

from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
# 注意，上面最后一行缺少一个 </li> 闭合标签,但etree.HTML模块可以自动修正HTML文本

# etree.HTML():构造了一个XPath解析对象，并对HTML文本进行自动修正
html = etree.HTML(text)

# etree.tostring()：输出修正后的结果，类型是bytes
result = etree.tostring(html)

print(type(result))  # bytes

print(result.decode())

print('*'*50)

# 获取class为item-1 li下的a的herf
ret1 = html.xpath("//li[@class='item-1']/a/@href")
print(ret1)

# 获取class为item-1 li下的a的文本
ret2 = html.xpath("//li[@class='item-1']/a/text()")
print(ret2)

# 每个li是一条新闻，把url和文本组成字典，存在一个问题，如果我们把first item改为item-1，并去除herf
for href in ret1:
    item = {}
    item["href"] = href
    item["title"] = ret2[ret1.index(href)]
    print(item)

print("*" * 100)
# 分组，根据li标签进行分组，对每一组继续写xpath
ret3 = html.xpath("//li[@class='item-1']")
print(ret3)
for i in ret3:
    item = {}
    item["title"] = i.xpath("a/text()")[0] if len(i.xpath("./a/text()")) > 0 else None
    item["href"] = i.xpath("./a/@href")[0] if len(i.xpath("./a/@href")) > 0 else None
    print(item)
