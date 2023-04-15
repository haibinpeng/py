# 作者: Michael(phb)
# 2023年04月13日22时10分07秒

from selenium import webdriver
import time


class DouBan:
    def __init__(self):
        self.url = "https://www.douban.com/"
        self.browser = webdriver.Chrome('H://Crawler//chromedriver.exe')

    def log_in(self):
        browser = self.browser
        browser.get(self.url)
        browser.implicitly_wait(3)

        # 重点1 要先切换到子框架
        browser.switch_to.frame(browser.find_elements_by_tag_name('iframe')[0])

        # 重点2 要先点击用账号密码登录的按钮，不然会找不到输入账号和密码的地方
        bottom1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
        bottom1.click()

        input1 = browser.find_element_by_id('username')
        input1.clear()
        input1.send_keys('18948796072')

        input2 = browser.find_element_by_id('password')
        input2.clear()
        input2.send_keys('Luke123')

        # 在这里sleep等一下，手动输入
        bottom = browser.find_element_by_class_name('account-form-field-submit ')
        bottom.click()
        time.sleep(10)

        # 获取cookie
        print(browser.get_cookies())
        cookies = {i["name"]: i["value"] for i in browser.get_cookies()}
        print(cookies)

        time.sleep(3)

        self.browser.quit()


if __name__ == "__main__":
    douban = DouBan()  # 实例化
    douban.log_in()  # 之后调用登陆方法
