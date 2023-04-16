# 作者: Michael(phb)
# 2023年04月16日17时00分57秒

from selenium import webdriver
import time


class DouBan:
    def __init__(self):
        self.url = 'https://www.douban.com/'
        self.driver = webdriver.Chrome('E:/crawler/day79/chromedriver.exe')

    def login(self):
        self.driver.get(self.url)

        self.driver.switch_to.frame(self.driver.find_element_by_tag_name('iframe'))
        self.driver.find_element_by_class_name('account-tab-account').click()

        self.driver.find_element_by_id('username').send_keys('13637009099')
        self.driver.find_element_by_id('password').send_keys('a5505616578')
        self.driver.find_element_by_class_name('account-form-field-submit').click()
        time.sleep(3)
        self.driver.save_screenshot('douban.png')

        # cookies = {i["name"]: i["value"] for i in self.driver.get_cookies()}

        self.driver.quit()


class QQEmail:
    def __init__(self):
        self.url = 'https://mail.qq.com//'
        self.driver = webdriver.Chrome('E:/crawler/day79/chromedriver.exe')

    def login(self):
        self.driver.get(self.url)

        self.driver.switch_to.frame(self.driver.find_element_by_id('login_frame'))
        self.driver.find_element_by_class_name('switch_btn').click()

        self.driver.find_element_by_id('u').send_keys('647494615')
        self.driver.find_element_by_id('p').send_keys('a5505616578')

        time.sleep(5)
        self.driver.find_element_by_class_name('login_button').click()
        time.sleep(3)
        self.driver.save_screenshot('qq_mail.png')

        # cookies = {i["name"]: i["value"] for i in self.driver.get_cookies()}

        self.driver.quit()


class ZhiHu:
    def __init__(self):
        self.url = 'https://www.zhihu.com/signin?next=%2F'
        self.driver = webdriver.Chrome('H:/Crawler/chromedriver.exe')

    def login(self):
        self.driver.get(self.url)

        self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[1]/div[2]').click()

        self.driver.find_element_by_name('username').send_keys('13637009099')
        self.driver.find_element_by_name('password').send_keys('a5505616578')
        self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/button').click()
        time.sleep(8)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/button').click()
        time.sleep(3)
        self.driver.save_screenshot('zhihu.png')

        # cookies = {i["name"]: i["value"] for i in self.driver.get_cookies()})

        # self.driver.quit()


class BStation:
    def __init__(self):
        self.url = 'https://passport.bilibili.com/login'
        self.driver = webdriver.Chrome('E:/crawler/day79/chromedriver.exe')

    def login(self):
        self.driver.get(self.url)

        self.driver.find_element_by_id('login-username').send_keys('13637009099')
        self.driver.find_element_by_id('login-passwd').send_keys('a5505616578')
        self.driver.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()
        time.sleep(8)
        self.driver.save_screenshot('b_station.png')

        # cookies = {i["name"]: i["value"] for i in self.driver.get_cookies()}

        self.driver.quit()


if __name__ == '__main__':
    # douban = DouBan()
    # qq_email = QQEmail()
    zhihu = ZhiHu()
    # b_staion = BStation()
    # douban.login()
    # qq_email.login()
    zhihu.login()
    # b_staion.login()
