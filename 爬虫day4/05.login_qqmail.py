# 作者: Michael(phb)
# 2023年04月13日22时59分26秒

from selenium import webdriver
import time

driver = webdriver.Chrome('H://Crawler//chromedriver.exe')
driver.get("https://mail.qq.com/")

# 切换到iframe
driver.switch_to.frame("login_frame")

driver.find_element_by_id("u").send_keys("2230933759")
driver.find_element_by_id("p").send_keys("lizhilong123")

bottom = driver.find_element_by_id("login_button")
bottom.click()

time.sleep(3)

driver.quit()
