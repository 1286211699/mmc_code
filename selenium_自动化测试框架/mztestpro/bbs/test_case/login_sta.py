#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 14:49
# @Author  : Xuegod Teacher For
# @File    : login_sta.py
# @Software: PyCharm
from time import sleep
import unittest,random,sys
sys.path.append('./models')
sys.path.append('./page_obj')
from mztestpro.bbs.test_case.models import myunit,function
from mztestpro.bbs.test_case.page_obj.loginPage import login

class loginTest(myunit.MyTest):
    '''社区登录测试'''
    def user_login_verify(self,username="",password = ""):
        login(self.driver).user_login(username,password)

    def test_login(self):
        '''用户名密码为空登录'''
        self.user_login_verify()
        po = login(self.driver)
        self.assertEqual(po.user_error_hint(),'账号不能为空')
        self.assertEqual(po.pawd_error_hint(),'密码不能为空')
        function.insert_img(self.driver,'user_pawd_empty.png')
    def test_login2(self):
        '''用户名正确，密码为空登录的'''
        self.user_login_verify(username='17611100746')
        po = login(self.driver)
        self.assertEqual(po.pawd_error_hint(),'密码不能为空')
        function.insert_img(self.driver,'pawd_empty.png')
    def test_login3(self):
        '''用户名为空密码不为空'''
        self.user_login_verify(password='mmc123456')
        po = login(self.driver)
        self.assertEqual(po.user_error_hint(),'账号不能为空')
        function.insert_img(self.driver,'user_empty.png')
    def test_login4(self):
        character = random.choice('abcedafdafads')
        username = '17611100746'+character
        self.user_login_verify(username=username,password='mmc123456')
        po = login(self.driver)
        self.assertEqual(po.pawd_error_hint(),'账号摩玛不匹配')
        function.insert_img(self.driver,'user_pawd_error.png')
    def test_login5(self):
        '''用户名密码正确'''
        self.user_login_verify(username='17611100746',password='mmv123456')
        sleep(2)
        po = login(self.driver)
        self.assertEqual(po.user_login_success(),'for')
        function.insert_img(self.driver,'user_pawd_ture.png')
if __name__ == '__main__':
    unittest.main()