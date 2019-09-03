#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 10:23
# @Author  : Xuegod Teacher For
# @File    : 斗鱼自动化_test.py
# @Software: PyCharm
from selenium import  webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.get('https://www.douyu.com/directory/all')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "DyListCover-intro")))

li_list = driver.find_elements_by_xpath("//ul[@class='layout-Cover-list']/li")
for li in li_list:
    print(li.find_element_by_xpath('.//h3').text)
# print(li_list)
# content_list = []
# for li in li_list:
#     print(li.text)

time.sleep(20)
driver.close()


