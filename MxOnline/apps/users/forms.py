#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 11:38
# @Author  : Xuegod Teacher For
# @File    : forms.py
# @Software: PyCharm
from django import forms
from captcha.fields import CaptchaField
class LoginForm(forms.Form):
    #用户名摩玛不为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)

    #验证码 字段里面可自定以错误提示信息
class RegisterForm(forms.Form):
    '''注册表单'''
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    #验证码
    captcha = CaptchaField()


#忘记密码
class ForgetPwdForm(forms.Form):
    '''忘记密码'''
    email = forms.EmailField(required=True)
    #验证码错误信息
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})

#重置密码的form
class ModifyPwdForm(forms.Form):
    '''重置密码'''
    password1 = forms.CharField(required=True,min_length=5)
    password2 = forms.CharField(required=True,min_length=5)