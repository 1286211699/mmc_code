#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 9:45
# @Author  : Xuegod Teacher For
# @File    : log_test.py
# @Software: PyCharm
import logging

#logger 收集日志
#haddler #输出日志的渠道

#定义一个日志收集器
my_logger  = logging.getLogger('python')
#设定级别,收集日志
my_logger.setLevel('DEBUG')
#定义一个输出渠道
ch = logging.StreamHandler()
ch.setLevel('DEBUG')

#文本格式
formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
#输出到文本
fh = logging.FileHandler('py.txt',encoding='utf-8')
fh.setLevel('DEBUG')
fh.setFormatter(formatter)
#两者对接
my_logger.addHandler(ch)
my_logger.addHandler(fh)
#收集日志
my_logger.debug('Python 真是好')
my_logger.error('Python 真不错')