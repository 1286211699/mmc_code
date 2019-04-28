#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 22:06
# @Author  : Xuegod Teacher For
# @File    : 05_TCP_client_test.py
# @Software: PyCharm
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9001))
print('已经链接')
info = ''
while info != 'exit':
    send_mes = input('>>>')
    s.send(send_mes.encode())
    if send_mes == 'exit':
        break
    info = s.recv(1024).decode()
    print('服务器:'+info)
s.close()