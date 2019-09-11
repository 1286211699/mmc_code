#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 15:50
# @Author  : Xuegod Teacher For
# @File    : myunit.py
# @Software: PyCharm
from selenium import webdriver
from .driver import browser
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def testDown(self):
        self.driver.quit()
