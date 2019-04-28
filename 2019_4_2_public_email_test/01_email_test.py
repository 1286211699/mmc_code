#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 14:44
# @Author  : Xuegod Teacher For
# @File    : 01_email_test.py
# @Software: PyCharm
# user = '3403073998@qq.com'
# pwd = 'ihenvpgtjinqchbd'
# to = '3403073998@qq.com'

import smtplib
from email.mime.text import MIMEText
#构造自己的发送者 接受者
from_addr = '3403073998@qq.com'
password = 'ihenvpgtjinqchbd' # pop3 授权码
to_addr = '3403073998@qq.com'
#构造发送的文本内容
msg = MIMEText('大家好 我是for，搭建想要领资料请到322群')
#对公服务器
smtp_server = 'smtp.qq.com'
#构造自己 的邮件服务器
server = smtplib.SMTP(smtp_server,25)
#登录自己的邮件
server.login(from_addr,password)
#发送邮件，第一个参数 返送这， 第二个参数我们是接受者， 打三个参数 发送的文本内容
server.sendmail(from_addr,to_addr,msg.as_string())
#关闭自己邮箱
server.close()


