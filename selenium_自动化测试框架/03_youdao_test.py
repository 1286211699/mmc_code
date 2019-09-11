#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 14:07
# @Author  : Xuegod Teacher For
# @File    : 03_youdao_test.py
# @Software: PyCharm
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.youdao.com')
driver.find_element_by_id('translateContent').send_keys('hello')
driver.find_element_by_id('translateContent').submit()
driver.close()