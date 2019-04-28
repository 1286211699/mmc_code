#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 21:51
# @Author  : Xuegod Teacher For
# @File    : 04_socker_server.py
# @Software: PyCharm
import socketserver

class MyHandle(socketserver.BaseRequestHandler):
    #__init__初始化函数
    def setup(self):
        print('muhandle is start ')
    #发送请求
    def handle(self):
        print(self.server)
        print('%s: %s is connectd'%self.client_address)

        recv = self.request.recv(521)

        print(recv.decode())

        self.request.send('I am server'.encode())
    #类似 del
    def finish(self):
        print('my handle is stop')
if __name__ == '__main__':
    #多线程处理客户端
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8005),MyHandle)
    #开启服务
    server.serve_forever()

