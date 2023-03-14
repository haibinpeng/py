# 作者: Michael(phb)
# 2023年03月12日21时48分42秒

from lxml import etree
import requests
from collections import defaultdict
import json


class XueYuan:
    def __init__(self):
        self.staet_url = "http://www.jikexueyuan.com/course/?pageNum=1"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
        }

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        html = etree.HTML(response.text)
        return html

    def get_first_page_content_list(self, url):
        html = self.parse_url(url)
        content_field = html.xpath('//div[@class="lesson-list"]/ul/li/div[@class="lesson-infor"]')
        data = defaultdict(list)
        for index, each in enumerate(content_field):
            mdict = {}
            title = each.xpath('h2/a/text()')[0]
            mdict['title'] = title
            info = (each.xpath('p/text()')[0]).strip()
            mdict['info'] = info
            time = (each.xpath('div/div[1]/dl/dd[1]/em/text()')[0]).replace('\t', '').replace('\n', ' ')
            mdict['time'] = time
            number = each.xpath('div/div[1]/em/text()')[0]
            mdict['number'] = number
            level = each.xpath('div/div[1]/dl/dd[2]/em/text()')[0]
            mdict['level'] = level
            data[index] = mdict
        return data

    def save_item(self, data):
        with open('xueyuan.txt', 'a', encoding='utf-8') as f:
            # json.dump(data, f, ensure_ascii=False, indent=2)
            f.write(json.dumps(data, ensure_ascii=False, indent=2))
            f.write('\n')

    def run(self):
        data = self.get_first_page_content_list(self.staet_url)
        self.save_item(data)


if __name__ == '__main__':
    xueyuan = XueYuan()
    data = xueyuan.run()
