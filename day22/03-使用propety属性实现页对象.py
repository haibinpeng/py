# 作者: Michael(phb)
# 2022年06月26日22时42分12秒
class Pager:
    def __init__(self, current_page):
        # 用户当前请求的页码
        self.current_page = current_page
        # 每页默认显示10条数据
        self.per_items = 10

    @property
    def start(self):
        return (self.current_page - 1) * self.per_items

    @property
    def end(self):
        return self.current_page * self.per_items


p = Pager(1)
print(p.start)
print(p.end)
