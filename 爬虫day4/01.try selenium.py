# 作者: Michael(phb)
# 2023年04月10日11时49分54秒

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

# 实例化一个浏览器
chrome_options = Options()

# 返回是否设置无头参数
chrome_options.add_argument('--headless')

chrome_options.add_argument('--disable-gpu')

# 无界面
# driver = webdriver.Chrome(executable_path='H://Crawler//chromedriver81.exe', chrome_options=chrome_options)

# 有界面
driver = webdriver.Chrome("H://Crawler//chromedriver81.exe")

# 设置窗口大小
driver.set_window_size(1920, 1080)

# 最大化窗口
# driver.maximize_window()

# 发送请求
driver.get("http://www.baidu.com")

# 进行页面截屏
driver.save_screenshot("./baidu.png")

# 元素定位的方法
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()

# driver 获取html字符串
# print(driver.page_source)  # 浏览器中elements的内容

print(driver.current_url)

# driver获取cookie并以dict保存
cookies = driver.get_cookies()
print(cookies)
print("*" * 100)
cookies = {i["name"]: i["value"] for i in cookies}
print(cookies)

# 退出浏览器
time.sleep(3)
driver.quit()
