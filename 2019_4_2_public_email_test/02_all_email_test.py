#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 14:56
# @Author  : Xuegod Teacher For
# @File    : 02_all_email_test.py
# @Software: PyCharm
from email.mime.text import MIMEText
#构造自己的发送者
from_addr = '3403073998@qq.com'
password = 'ihenvpgtjinqchbd' # pop3 授权码
to_addr = '3403073998@qq.com'
#构造自己邮件信息，字符串，格式，字符集
msg = MIMEText('<html><body><h1>你好</h1>' +
               '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
               '</body></html>','html','utf-8'
               )
#构造自己邮件主题
msg['Subject'] = '这是一个发送的测试'
msg['From'] = from_addr
msg['To'] = to_addr

import smtplib
#构造自己的邮箱
server = smtplib.SMTP('smtp.qq.com',25)
#登录自己的邮箱
server.login(from_addr,password)
#利用邮箱发送文本
server.sendmail(from_addr,to_addr,msg.as_string())
#关闭自己的邮箱
server.close()