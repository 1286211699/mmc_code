#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 15:26
# @Author  : Xuegod Teacher For
# @File    : 02_baidu_down_test.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
if os.path.exists('1.txt'):
    os.remove('1.txt')
driver = webdriver.Chrome()

driver.implicitly_wait(30)
driver.get('http://www.baidu.com')

WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.ID,'kw')))
driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
#保存数据
def parse_data(e_item):
    with open('1.txt','a',encoding='utf-8') as f:

        for e in e_item:
            print(e.find_element_by_tag_name('a').text)
            f.write(e.find_element_by_tag_name('a').text+'\n')
def main():
    for i in range(1,5):
        time.sleep(1)
        WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.ID,"page")))
        e_item = driver.find_elements_by_xpath('//div[@class="result c-container "]')
        parse_data(e_item)
        driver.find_element_by_xpath(f"//div[@id='page']/descendant::span[text()='{i}']").click()
main()