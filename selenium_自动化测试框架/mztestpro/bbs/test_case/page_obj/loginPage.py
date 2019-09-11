#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 10:20
# @Author  : Xuegod Teacher For
# @File    : loginPage.py
# @Software: PyCharm
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from mztestpro.bbs.test_case.page_obj.base import Page
from time import sleep
from mztestpro.bbs.test_case.page_obj.jiyan import CrackGeetest
class login(Page,CrackGeetest):
    '''
    用户登录界面
    '''
    url = '/'
    #action
    bbs_login_user_loc = (By.XPATH,'//div[@id="mzCust"]/div/img')
    bbs_login_button_loc = (By.ID,'mzLogin')

    def bbs_login(self):
        self.find_element(*self.bbs_login_user_loc).click()
        sleep(1)
        self.find_element(*self.bbs_login_button_loc).click()
    login_username_loc = (By.ID,'account')
    login_password_loc = (By.ID,'password')
    login_button_loc = (By.ID,'login')

    #登录用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)

    #登录密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)

    #登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    #定义统一登录入口,魅族登录账号和密码为 17611100746 mmc123456
    def user_login(self,username= '17611100746',password= 'mmc123456'):
        self.open()
        self.bbs_login()
        self.login_username(username)
        self.login_password(password)
        # self.crack()
        self.login_button()
        sleep(1)
    user_error_hint_loc = (By.XPATH,'//span[@for="account"]')
    paswd_error_hint_loc = (By.XPATH,'//span[@for="password"]')
    user_login_success_loc = (By.ID,'mzCustName')

    #用户名错误提示
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc)

    #密码错误其实
    def pawd_error_hint(self):
        return self.find_element(*self.paswd_error_hint_loc)

    #登录成功提示
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc)
from mztestpro.bbs.test_case.models.driver import browser
if __name__ == '__main__':

    e = login(browser())
    e.user_login()