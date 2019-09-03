#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 14:45
# @Author  : Xuegod Teacher For
# @File    : 01_sel_test.py
# @Software: PyCharm
#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
#初始化一个股沟浏览器
driver = webdriver.Chrome()
# driver.implicitly_wait(30)
#get请求后面加请求地址
driver.get('http://www.baidu.com')
# time.sleep(1)
try:
    #定位input标签 并在内部进行输入
    WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.ID,'kw')))
    driver.find_element_by_id('kw').send_keys('python')
    driver.find_element_by_id('kw').clear()
    driver.find_element_by_id('kw').send_keys('selenium')
    driver.find_element_by_id('su').click()
    # time.sleep(8)
    #打印当前浏览器界面中的所有html
    print(driver.page_source)
except Exception as e:
    print(e)
finally:
    driver.close()