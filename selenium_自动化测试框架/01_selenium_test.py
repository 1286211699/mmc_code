#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 11:28
# @Author  : Xuegod Teacher For
# @File    : 01_selenium_test.py
# @Software: PyCharm
import time
from selenium import webdriver
#初始化一个webdriver，浏览器
driver = webdriver.Chrome()
#通过浏览器请求括号中的网址
driver.get('http://www.baidu.com')
#打印具体数据
print('浏览器实战')
#强制让程序等待
time.sleep(2)
#关闭当前窗口
driver.close()

# #访问百度首页
# first_url = 'http://www.baidu.com'
# print('now access %s'%first_url)
# driver.get(first_url)
#
# #访问新闻页面
# second_url = 'http://news.baidu.com'
# print('now access %s'%second_url)
# driver.get(second_url)
#
# #返回后退到百度首页
# print('back to %s'%first_url)
# driver.back()
# time.sleep(2)

#前进到新闻也
# print('forward to %s '%second_url)
# driver.forward()
# time.sleep(2)
# driver.quit()