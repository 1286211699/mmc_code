#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 15:46
# @Author  : Xuegod Teacher For
# @File    : driver.py
# @Software: PyCharm
from selenium.webdriver import Remote
from selenium import webdriver

def browser():
    driver = webdriver.Chrome()
    return driver
if __name__ == '__main__':
    dr = browser()
    dr.get('http://www.baidu.com')
    dr.quit()

