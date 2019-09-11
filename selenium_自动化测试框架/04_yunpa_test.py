#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 14:10
# @Author  : Xuegod Teacher For
# @File    : 04_yunpa_test.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()

driver.get('http://www.baidu.com')
#定位到操作标签
right_click = driver.find_element_by_class_name('bri')
#进行动态操作
ActionChains(driver).double_click(right_click).perform()
time.sleep(2)
driver.quit()