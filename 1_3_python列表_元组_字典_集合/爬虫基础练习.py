#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 19:59
# @Author  : Xuegod Teacher For
# @File    : 爬虫基础练习.py
# @Software: PyCharm

#操作指导 注意copy这段代码在你的pycharm上！自己创建py文件
#需要安装 requests这个模块 在咱们的cmder下 pip install requests 就好


import  requests,time
from urllib import request #网络请求

url = 'http://image.so.com/zj?ch=beauty&sn=60&listtype=new&temp=1'
#模拟请求头
headers= {
    'Referer': 'http://image.so.com/z?ch=beauty',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}
#给服务器发送信息，这是一个字符串 可换行的字符串
str_data = '''ch: beauty
sn: 120
listtype: new
temp: 1
'''
# str_data = {'ch':'beauty','sn':'120'}
#数据清洗
send_data = {}#定义一个空子典
for data in str_data.splitlines():#进行遍历以行进行分割
    # print('data:',data)
    line_data = data.split(': ')# 每个数据进行分割': '
    # print(line_data)
    if len(line_data) == 2:#len获取元素的个数
        key,value = line_data#序列解包赋值 a,b = [1,2]
        if key and value:#判断 是否有值
            send_data[key] = value
print(send_data)
# #访问服务器，不用管
response = requests.get(url,headers=headers,params=send_data)
# #服务器返回数据 把它变成python可操作对象，先理解为 python字典
json_data = response.json()['list']
# print(json_data)
for src in json_data:
#    #获取字典中的qhimg_url
    image_url = src['qhimg_url']
    print(image_url)
    try:#抓捕异常
        image_name = image_url[-8:]#字符窜切片
        #将图片数据保存在本地
        request.urlretrieve(url=image_url,filename=image_name)
    except Exception as e:
        print(e)
    else:
        #format 字符串格式化
        print('{} is download'.format(image_name))
