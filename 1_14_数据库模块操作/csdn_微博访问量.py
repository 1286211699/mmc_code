#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 9:44
# @Author  : Xuegod Teacher For
# @File    : csdn_微博访问量.py
# @Software: PyCharm

# from s\
import time,os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import json1

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=chrome_options)
urllist = [
    'https://blog.csdn.net/Smile_Mr/article/details/105531204',
    'https://blog.csdn.net/Smile_Mr/article/details/105115235',
    'https://blog.csdn.net/Smile_Mr/article/details/104019930',
    'https://blog.csdn.net/Smile_Mr/article/details/104019930',
    'https://blog.csdn.net/Smile_Mr/article/details/87694811',
    'https://blog.csdn.net/Smile_Mr/article/details/85773640',
    'https://blog.csdn.net/Smile_Mr/article/details/83108328',
    'https://blog.csdn.net/Smile_Mr/article/details/94400675',
    'https://blog.csdn.net/Smile_Mr/article/details/86537239'

]
try:
    for j in range(1000000):
        for i in urllist:
            driver.get(i)
            time.sleep(2)
        driver.close()
except:
    time.sleep(5)
    os.system('python csdn_微博访问量.py')



