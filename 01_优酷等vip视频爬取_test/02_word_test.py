#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 14:52
# @Author  : Xuegod Teacher For
# @File    : 02_word_test.py
# @Software: PyCharm
from wordcloud import WordCloud
#打开并读取所有文本
f  = open('1.txt','r').read()
#生成测孕，
wc = WordCloud(
    background_color='white',#控制背景色
    width=500,#本菁长度
    height=366,#北京高度
    margin=2,#词语之间的间隔
).generate(f)#升窗词云
#保存文件格式为图片
wc.to_file('0.jpg')