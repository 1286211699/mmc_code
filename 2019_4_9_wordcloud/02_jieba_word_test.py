#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 10:40
# @Author  : Xuegod Teacher For
# @File    : 02_jieba_word_test.py
# @Software: PyCharm

from urllib import request
import time
from lxml import etree#pip install lxml
#基础url
url = 'https://read.qidian.com/chapter/9r9u8W1evJUCpOPIBxLXdQ2/eSlFKP1Chzg1'
#请求头
headers = {
    'Referer': 'https://read.qidian.com/chapter/9r9u8W1evJUCpOPIBxLXdQ2/eSlFKP1Chzg1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
}
#发送网路请求
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
#生成文本网上的html
content = response.read().decode()
#转换为xpath可匹配的到的文本
xpath_content = etree.HTML(content)
#利用xpath获取到文本内容
new_content = xpath_content.xpath('//*[@id="chapter-382639401"]/div/div/p/text()')
#保存到本地
with open('3.txt','w',encoding='utf-8') as f:
    for i in new_content:
        f.writelines(i.strip()+'\n')











