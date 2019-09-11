#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 14:26
# @Author  : Xuegod Teacher For
# @File    : 05_baidu_test.py
# @Software: PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
#编写
driver.find_element_by_id('kw').send_keys('seleniumm')
time.sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
time.sleep(1)
driver.find_element_by_id('kw').send_keys(Keys.SPACE)
driver.find_element_by_id('kw').send_keys('教程')

time.sleep(1)
#类似ctrl +a 全选输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
time.sleep(1)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
time.sleep(1)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
time.sleep(1)

# driver.find_element_by_id('su').submit()
driver.find_element_by_id('su').send_keys(Keys.ENTER)

driver.close()