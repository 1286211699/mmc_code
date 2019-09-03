#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 14:45
# @Author  : Xuegod Teacher For
# @File    : 01_email_test.py
# @Software: PyCharm
import smtplib # 邮件发送
from email.mime.text import MIMEText #构造自己邮箱的正文文本
#构造发件人
user = '3403073998@qq.com'
pwd = 'ihenvpgtjinqchbd' #pop3 授权码
to = '3403073998@qq.com'
#构造正文文本
msg = MIMEText('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>测试</title>
</head>
<body>
<h1>你好</h1>
<p>send by <a href="http://www.baidu.com">python</a></p>
</body>
</html>''','html','utf-8')

msg['Subject'] = '这是一个邮件测试'
msg['From'] = user
msg['To'] = to

#腾讯服务器
smtp_server = 'smtp.qq.com'
#创建自己的邮箱服务器
server = smtplib.SMTP(smtp_server,25)
#登录自己的服务器
server.login(user,pwd)
#发送邮件
server.sendmail(user,to,msg.as_string())
#关闭自己的服务器
server.close()

