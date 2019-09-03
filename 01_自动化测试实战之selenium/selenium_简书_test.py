#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 10:34
# @Author  : Xuegod Teacher For
# @File    : selenium_简书_test.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
browser = webdriver.Chrome()
browser.get('https://www.jianshu.com/')

for i in range(3):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
#
# button = browser.find_element_by_class_name('load-more')
# if button:
def save_data(titles):
    with open("2.txt", "w", encoding="utf-8") as f:
        for t in titles:
            try:
                f.write(t.text + '\t' + t.get_attribute("href"))
                f.write("\n")
            except TypeError:
                pass
for i in range(10):
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "load-more")))
        button = browser.find_element_by_class_name('load-more')
        button.click()
        time.sleep(2)
    except:
        pass#
    titles = browser.find_elements_by_class_name("title")

    save_data(titles)


