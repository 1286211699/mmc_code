# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 16:37
# @Author  : for 
# @File    : begin.py
# @Software: PyCharm
from scrapy import cmdline

cmdline.execute(('scrapy crawl zhihu').split())