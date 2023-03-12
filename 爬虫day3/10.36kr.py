# 作者: Michael(phb)
# 2023年03月12日17时34分20秒

import requests
import re
import json


class Html36kr:
    def __init__(self):
        self.start_url = "http://36kr.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
        }

    def parse_url(self, url):
        """发送请求"""
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_first_page_content_list(self, html_str):
        """提取第一页的数据"""
        content_list = re.findall(r"<a class=\"article-item-title weight-bold\".*?>(.*?)</a>", html_str, re.S)
        return content_list

    def save_content_list(self, content_list):
        """保存"""
        with open("36kr.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))  # 可直接用json.dump()
                f.write("\n")
        print("保存成功")

    def run(self):  # 实现主要逻辑
        # 1.start_url
        # 2.发送请求，获取响应
        html_str = self.parse_url(self.start_url)
        # 3.提取数据
        content_list = self.get_first_page_content_list(html_str)
        # 4.保存
        self.save_content_list(content_list)


if __name__ == '__main__':
    kr = Html36kr()
    kr.run()
