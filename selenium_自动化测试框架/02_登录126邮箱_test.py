#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 13:37
# @Author  : Xuegod Teacher For
# @File    : 02_登录126邮箱_test.py
# @Software: PyCharm
#表单切换
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get('https://www.126.com/')

driver.find_element_by_id('switchAccountLogin').click()
time.sleep(1)

xf = driver.find_element_by_tag_name('iframe')
#进行fram切换 一般都是以id 和class进行定位的
driver.switch_to.frame(xf)
print(driver.page_source)


driver.find_element_by_xpath("//*[@name='email']").send_keys('m1286211699')
driver.find_element_by_xpath("//*[@name='password']").send_keys('mmc123456')
# driver.find_element_by_id('auto-id-1567748313992').send_keys('m1286211699')
# driver.find_element_by_id('auto-id-1567748313995').send_keys('mmc123456')


driver.find_element_by_id('dologin').click()

time.sleep(2)
driver.close()