#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 14:55
# @Author  : Xuegod Teacher For
# @File    : 01_下拉三次_test.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.by import By
#初始化一个浏览器
driver = webdriver.Chrome()
driver.get('https://www.jianshu.com')
# driver.find_element_by_id('kw').send_keys('python')
# driver.find_element_by_id('su').click()


for i in range(3):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(4)
for i in range(10):
    try:

        WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'load-more')))
        button = driver.find_element_by_class_name('load-more').click()
        time.sleep(2)
    except:
        pass

