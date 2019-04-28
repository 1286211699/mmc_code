# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 14:51
# @Author  : for 
# @File    : 01_360_image_test.py
# @Software: PyCharm
import requests,time
from urllib import request
#基础url
url = 'http://image.so.com/zj?ch=beauty&sn=210&listtype=new&temp=1'
#模拟浏览器请求头
headers = {
    'Referer': 'http://image.so.com/z?ch=beauty',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
}
#给服务器发送data
str_data = '''ch: beauty
sn: 240
listtype: new
temp: 1
'''
#简单是数据清洗
send_data = {}
for data in str_data.splitlines():
    # print('这是data:',data)
    line_data = data.split(': ')
    # print(line_data)
    if len(line_data) == 2:
        key,value = line_data#序列解包赋值
        if key and value:
            send_data[key] = value
#模拟浏览器访问服务器
response = requests.get(url,headers=headers,params=send_data)
#响应的数据变成python可操作对象
json_data = response.json()['list']
#美剧的方法遍历
for index,src in enumerate(json_data):
    #获取到每一个url地址
    image_url = src['qhimg_url']
    try:
        #给本地文件一个name
        image_name = './360_image/'+image_url[-8:]
        #吧网路上的数据下载到本地
        request.urlretrieve(url = image_url,filename=image_name)
    except Exception as e:
        print(e)
    else:
        print('{} is download'.format(image_name))



