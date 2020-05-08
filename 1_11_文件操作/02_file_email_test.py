#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 10:38
# @Author  : Xuegod Teacher For
# @File    : 02_file_email_test.py
# @Software: PyCharm
import smtplib,time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

user = '3403073998@qq.com'
pwd = 'ihenvpgtjinqchbd'
to = '3403073998@qq.com'

msg = MIMEMultipart()
msg['Subject'] = '这是一个测试'
msg['From'] = user
msg['To'] = to

part = MIMEText('大家上午好')
msg.attach(part)

part = MIMEApplication(open('0.jpg','rb').read())
part.add_header('content-disposition', 'attachment', filename='0.jpg')

msg.attach(part)

try:
    s = smtplib.SMTP('smtp.qq.com',timeout=30)

    s.login(user,pwd)

    s.sendmail(user,to,msg.as_string())

except Exception as e:
    print(e)
time.sleep(1)
s.close()







