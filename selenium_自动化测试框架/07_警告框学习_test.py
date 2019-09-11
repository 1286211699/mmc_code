#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 15:08
# @Author  : Xuegod Teacher For
# @File    : 07_警告框学习_test.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.implicitly_wait('30')
driver.get('http:www.baidu.com')
#鼠标悬停
link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()

#打开搜索设置
driver.find_element_by_link_text('搜索设置').click()
#给定时间让标签能加载过来
time.sleep(1)

#保存设置
cl = driver.find_element_by_class_name('prefpanelgo')
ActionChains(driver).move_to_element(cl).click(cl).perform()


#接受警告蓝
driver.switch_to.alert.accept()
driver.close()