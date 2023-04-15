# 作者: Michael(phb)
# 2023年04月13日22时23分33秒

from selenium import webdriver

driver = webdriver.Chrome('H://Crawler//chromedriver.exe')

driver.get(
    "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=python&rsv_pq=f47861160000c0da&rsv_t=42e7HUi7RYSatovzyPd%2BTB6mgcb5zmOLt7TINK5YNZyRoCkhsXr3gWFSy5k&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=6&rsv_sug1=6&rsv_sug7=100&rsv_sug2=0&inputT=970&rsv_sug4=971&rsv_sug=2"
)

# find_element_by_link_text,需要指定标签内全部的文本内容才能够进行定位
# 要获取元素属性class的值，就可以使用element.get_attribute(‘class’)
print(driver.find_element_by_link_text("下一页>").get_attribute("href"))

# find_element_by_partial_link_text,指定某部分文本即可定位成功,文本中包含下一页的a标签
print(driver.find_element_by_partial_link_text("下一页").get_attribute("href"))

driver.quit()
