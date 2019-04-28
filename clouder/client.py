#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 13:59
# @Author  : Xuegod Teacher For
# @File    : client.py
# @Software: PyCharm
import socket

s=socket.socket()
host=socket.gethostname()
port=3456
s.connect((host,port))
cmd=input(">>>")
s.sendall(cmd.encode())
data=s.recv(1024)
print(data.decode())
s.close()
