#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 15:10
# @Author  : Xuegod Teacher For
# @File    : 03_email_test.py
# @Software: PyCharm
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

user = '3403073998@qq.com'
pwd = 'ihenvpgtjinqchbd'
to = '3403073998@qq.com'

msg = MIMEMultipart()

msg['Subject'] = '这个是咱们的的test'
msg['From'] = user
msg['To'] = to

part = MIMEText('这个我是正文文本')
msg.attach(part)

part =MIMEApplication(open('1.jpg','rb').read())
part.add_header('content-disposition', 'attachment', filename='1.jpg')
msg.attach(part)

part =MIMEApplication(open('1.gif','rb').read())
part.add_header('content-disposition', 'attachment', filename='1.gif')
msg.attach(part)

try:
    s = smtplib.SMTP('smtp.qq.com',timeout=30)
    s.login(user,pwd)
    s.sendmail(user,to,msg.as_string())
except Exception as e:
    print(e)
finally:
    s.close()










