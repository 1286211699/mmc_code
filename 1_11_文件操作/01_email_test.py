#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 10:18
# @Author  : Xuegod Teacher For
# @File    : 01_email_test.py
# @Software: PyCharm
import smtplib
from email.mime.text import MIMEText
# user = '3403073998@qq.com'
# pwd = 'ihenvpgtjinqchbd'
# to = '3403073998@qq.com'
#构造发件人，收件人，pop3 授权码
from_addr = '3403073998@qq.com'
password = 'ihenvpgtjinqchbd'
to_addr = '3403073998@qq.com'
#构造邮箱的正文内容
msg = MIMEText('<html><body><h1>你好</h1>' +
               '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
               '</body></html>','html','utf-8'
               )
msg['Subject'] = '大家上午好'
msg['From'] = from_addr
msg['To'] = to_addr


#提取腾讯开放服务器
smtp_server = 'smtp.qq.com'
#构造自己的服务器，25端口是邮件传输的默认端口
server = smtplib.SMTP(smtp_server,25)
#登录自己的服务器
server.login(from_addr,password)
#发送邮件，第一个参数，发件人，第二个参数 接收人，第三个参数 发送的内容
server.sendmail(from_addr,to_addr,msg.as_string())
#关闭自己的邮件服务器
server.close()





