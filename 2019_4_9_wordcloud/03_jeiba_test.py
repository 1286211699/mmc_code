#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 10:49
# @Author  : Xuegod Teacher For
# @File    : 03_jeiba_test.py
# @Software: PyCharm
import jieba
from scipy.misc import imread
from wordcloud import WordCloud,STOPWORDS

back_color = imread('9.png')

wc = WordCloud(
    background_color='white',
    max_words=2000,
    mask = back_color,
    max_font_size=100,
    stopwords=STOPWORDS.add('国'),
    font_path='C:\Windows\Fonts\simfang.ttf',
    random_state=42,
)

text = open('3.txt',encoding='utf-8').read()

def stop_word(texts):
    word_list = []
    word_genrtator = jieba.cut(texts,cut_all=False)
    for word in word_genrtator:
        word_list.append(word)
    print(word_list)
    return ' '.join(word_list)
text = stop_word(text)

wc.generate(text)
wc.to_file('maikou.png')