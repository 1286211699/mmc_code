#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 15:03
# @Author  : Xuegod Teacher For
# @File    : 02_send_eamil_test.py
# @Software: PyCharm
import smtplib,time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
#构造发件人
user = '3403073998@qq.com'
pwd = 'ihenvpgtjinqchbd' #pop3 授权码
to = '3403073998@qq.com'

msg = MIMEMultipart()

msg['Subject'] = '这是一个测试'
msg['From'] = user
msg['To'] = to

part = MIMEText('这是一个附件测试')
msg.attach(part)

part = MIMEApplication(open('0.jpg','rb').read())
part.add_header('content-disposition', 'attachment', filename='0.jpg')
msg.attach(part)

try:
    s = smtplib.SMTP('smtp.qq.com',25,timeout=30)
    s.login(user,pwd)
    s.sendmail(user,to,msg.as_string())
except Exception as e:
    print(e)

finally:
    s.close()


