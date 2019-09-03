#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 10:40
# @Author  : Xuegod Teacher For
# @File    : 02_baidu_test.py
# @Software: PyCharm
from selenium import webdriver
import time
import selenium.webdriver.support.ui as ui  ###智能等待调用的类，as是重命名

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
time.sleep(1)
try:
    driver.find_element_by_id('kw').send_keys('python')
    driver.find_element_by_id('su').click()
    time.sleep(3)

except Exception as e:
    print(e)
finally:
    driver.close()