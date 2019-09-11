#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 14:48
# @Author  : Xuegod Teacher For
# @File    : 06_多窗口切换_test.py
# @Software: PyCharm
from selenium import webdriver
import time
driver = webdriver.Chrome()
#隐世等待
driver.implicitly_wait(30)

driver.get('http:/www.baidu.com')

#获取百度搜索的句柄,获取当前的窗口网页
search_windows = driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()
#获取当前所有打开的窗口的句柄
all_handles = driver.window_handles

#循环判断
for handle in all_handles:
    if handle == search_windows:
        driver.switch_to.window(handle)
        print('now search window')
        driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
        driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys('18737310377')
        driver.find_element_by_id('TANGRAM__PSP_10__password').send_keys('mama521')
        driver.find_element_by_id('TANGRAM__PSP_10__submit').click()

#投入注册窗口
for handle in all_handles:
    if handle != search_windows:
        driver.switch_to.window(handle)
        print('now register window')
        driver.find_element_by_name('userName').send_keys('m18737310377')
        driver.find_element_by_name('phone').send_keys('18737310377')
        driver.find_element_by_name('password').send_keys('mama521')
        time.sleep(2)





driver.quit()