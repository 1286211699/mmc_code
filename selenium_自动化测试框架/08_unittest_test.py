#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 13:51
# @Author  : Xuegod Teacher For
# @File    : 08_unittest_test.py
# @Software: PyCharm
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
import unittest
class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = 'http://www.baidu.com/'
    def test_baidu_search(self):
        '''搜索关键字:HTMLTestRunner'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('kw').send_keys('HTMLTestRunner')
        driver.find_element_by_id('su').click()
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu('test_baidu_search'))
    fp = open('./result.html','wb')
    runner = HTMLTestRunner(stream=fp,title='百度搜索测试报告',description='用例这行情况')
    runner.run(testunit)
    fp.close()