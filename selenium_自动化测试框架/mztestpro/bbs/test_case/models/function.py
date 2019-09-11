#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 16:02
# @Author  : Xuegod Teacher For
# @File    : function.py
# @Software: PyCharm
from selenium import webdriver
import os
def insert_img(driver,file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split('/test_case')[0]

    file_path = base+'/report/image/'+file_name
    # print(file_path)
    #浏览器截屏，获取资源
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    insert_img(driver,'baidu.png')
    driver.quit()