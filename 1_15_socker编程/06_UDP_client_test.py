#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 22:19
# @Author  : Xuegod Teacher For
# @File    : 06_UDP_client_test.py
# @Software: PyCharm
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.connect(('127.0.0.1',9002))

print('connection...')
info = ''
while info != 'exit':
    send_mes = input('>>>')
    s.sendall(send_mes.encode())
    info = s.recv(1024).decode()
    print('服务器:'+info)
s.close()