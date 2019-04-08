#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/5 10:32
# @Author  : Xuegod Teacher For
# @File    : 04_spawn_360_test.py
# @Software: PyCharm

from gevent import monkey
monkey.patch_all()
import requests,gevent
from urllib import request #把图片下载到本地
def downlaod_img(num):
    print('start download')
    url = 'http://image.so.com/zj?ch=beauty&sn=180&listtype=new&temp=1'
    headers = {
        'Referer': 'http://image.so.com/z?ch=beauty',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
    }
    str_data = '''ch: beauty
    sn: 180
    listtype: new
    temp: 1'''

    send_data = {}#发送给服务器的
    for data in str_data.splitlines():#行进行分割
        line_data = data.split(': ')#以： 进行分割
        if len(line_data) == 2:#判断列表中的数据涨肚是不是为2
            key,value = line_data#序列解包赋值
            if key and value:#如果有值
                send_data[key] = value#字典的修改
    send_data['sn'] = eval(str(num)+'*'+'30')#执行数据加成
    response = requests.get(url,headers=headers,params=send_data)#给服务器发送网略请求
    json_data = response.json()['list']#吧网上的事json数据转变为Python可操作对象
    for index,src in enumerate(json_data):#枚举方法 给岁引号 ，然后获取数据
        image_url = src['qhimg_url']#提取数据当中的imgul了地址
        try:
            image_name = './360_image/'+image_url[-8:]#给本地文件一个格式名文件名
            request.urlretrieve(url = image_url,filename=image_name)#吧网上的数据保存到本机
        except Exception as e:
            print(e)
        else:
            print('{} is download'.format(image_name))#用字符串格式化操作
    print('image is download')#告说我这一组数据已经执行完毕
if __name__ == '__main__':
    num = int(input('请输入你想要的组：'))
    gevent.joinall([gevent.spawn(downlaod_img,i)for i in range(1,num+1)])#开启多任务下载


