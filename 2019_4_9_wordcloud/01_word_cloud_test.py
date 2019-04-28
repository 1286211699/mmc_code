#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 10:10
# @Author  : Xuegod Teacher For
# @File    : 01_word_cloud_test.py
# @Software: PyCharm

from wordcloud import WordCloud
#打开文件读取内容
f = open('2.txt','r',encoding='utf-8').read()
#wordcloud生成词云
wc = WordCloud(
    background_color='white',
    width=500,
    height=366,
    font_path='C:/Windows/Fonts/STFANGSO.ttf',
    margin=2
).generate(f)
#词云保存到本地
wc.to_file('0.jpg')




#
# from wordcloud import WordCloud
# from scipy.misc import imread
#
#
# f = open('1.txt','r').read()
# #解析图片将图片转弯位数组
# mk = imread('9.png')
#
# wc = WordCloud(
#     mask=mk,
#     background_color='white',
#     width=500,
#     height=366,
#     margin=2
# ).generate(f)
#
# wc.to_file('1.jpg')









