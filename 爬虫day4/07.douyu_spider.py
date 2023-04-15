# 作者: Michael(phb)
# 2023年04月13日23时06分08秒

import json
from selenium import webdriver
import time


class DouYuSpider:
    def __init__(self):
        self.start_url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome('H://Crawler//chromedriver.exe')

    def get_content_list(self):
        content_list = []
        try:
            for i in range(1000):
                if i == 0:
                    continue
                item = {}
                item["room_img"] = self.driver.find_element_by_xpath(
                    "//ul[@class='layout-Cover-list']/li[" + str(i) + "]/div/a[1]/div[1]/div[1]/img").get_attribute(
                    "src")
                item["room_title"] = self.driver.find_element_by_xpath(
                    "//ul[@class='layout-Cover-list']/li[" + str(i) + "]/div/a[1]/div[2]/div[1]/h3").get_attribute(
                    "title")
                item["room_cate"] = self.driver.find_element_by_xpath(
                    "//ul[@class='layout-Cover-list']/li[" + str(i) + "]//span[@class='DyListCover-zone']").text
                item["anchor_name"] = self.driver.find_element_by_xpath(
                    "//ul[@class='layout-Cover-list']/li[" + str(i) + "]/div/a[1]/div[2]/div[2]/h2").text
                item["watch_num"] = self.driver.find_element_by_xpath(
                    "//ul[@class='layout-Cover-list']/li[" + str(i) + "]/div/a[1]/div[2]/div[2]/span").text
                content_list.append(item)
        except:
            pass
        # for li in li_list:
        #     item = {}
        #     li.find_element_by_class_name("DyImg-content is-normal").get_attribute("src")
        #     item["room_img"] = li.find_element_by_xpath(
        #         ".//div/a[1]/div[1]/div[1]/img").get_attribute("src")
        #     item["room_title"] = li.find_element_by_xpath("./a").get_attribute("title")
        #     item["room_cate"] = li.find_element_by_xpath(".//span[@class='DyListCover-zone']").text
        #     item["anchor_name"] = li.find_element_by_xpath(".//span[@class='DyListCover-userIcon']").text
        #     item["watch_num"] = li.find_element_by_xpath(".//span[@class='DyListCover-hotIcon']").text
        #     print(item)
        #     content_list.append(item)
        # 获取下一页的元素
        next_url = self.driver.find_elements_by_xpath("//a[@class='shark-pager-next']")
        next_url = next_url[0] if len(next_url) > 0 else None
        return content_list, next_url

    def save_content_list(self, content_list):
        f = open("douyu.txt", "a")
        for content in content_list:
            json.dump(content, f, ensure_ascii=False, indent=2)
            f.write("\n")
        f.close()

    def run(self):  # 实现主要逻辑
        # 1.start_url
        # 2.发送请求，获取响应
        self.driver.get(self.start_url)
        # 3.提取数据，提取下一页的元素
        content_list, next_url = self.get_content_list()
        # 4.保存数据
        self.save_content_list(content_list)
        # 5.点击下一页元素，循环
        while next_url is not None:
            next_url.click()
            time.sleep(10)
            content_list, next_url = self.get_content_list()
            self.save_content_list(content_list)


if __name__ == '__main__':
    douyu = DouYuSpider()
    douyu.run()
