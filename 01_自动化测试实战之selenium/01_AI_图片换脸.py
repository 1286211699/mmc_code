#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 10:01
# @Author  : Xuegod Teacher For
# @File    : 01_AI_图片换脸.py
# @Software: PyCharm
import requests
import simplejson
import json
import base64

def find_face(imgpath):
    print("finding")
    http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
    data = {"api_key": 'gFtQbShDc83sYVdC8h36zjP0ooZ0E9ii',
            "api_secret": 'HbqIaYmdX_unfha_O1sfGCY00YQaDIpO', "image_url": imgpath, "return_landmark": 1}
    files = {"image_file": open(imgpath, "rb")}
    response = requests.post(http_url, data=data, files=files)
    req_con = response.content.decode('utf-8')
    req_dict = json.JSONDecoder().decode(req_con)
    this_json = simplejson.dumps(req_dict)
    this_json2 = simplejson.loads(this_json)
    faces = this_json2['faces']
    list0 = faces[0]
    rectangle = list0['face_rectangle']
    # print(rectangle)

    return rectangle
#number表示换脸的相似度
def merge_face(image_url_1,image_url_2,image_url,number):
    ff1 = find_face(image_url_1)
    ff2 = find_face(image_url_2)
    rectangle1 = str(str(ff1['top']) + "," + str(ff1['left']) + "," + str(ff1['width']) + "," + str(ff1['height']))
    rectangle2 = str(ff2['top']) + "," + str(ff2['left']) + "," + str(ff2['width']) + "," + str(ff2['height'])
    url_add = "https://api-cn.faceplusplus.com/imagepp/v1/mergeface"
    f1 = open(image_url_1, 'rb')
    f1_64 = base64.b64encode(f1.read())
    f1.close()
    f2 = open(image_url_2, 'rb')
    f2_64 = base64.b64encode(f2.read())
    f2.close()
    data = {"api_key": 'gFtQbShDc83sYVdC8h36zjP0ooZ0E9ii', "api_secret": 'HbqIaYmdX_unfha_O1sfGCY00YQaDIpO',
            "template_base64": f1_64, "template_rectangle": rectangle1,
            "merge_base64": f2_64, "merge_rectangle": rectangle2, "merge_rate": number}
    response = requests.post(url_add, data=data)
    req_con = response.content.decode('utf-8')
    req_dict = json.JSONDecoder().decode(req_con)
    result = req_dict['result']
    imgdata = base64.b64decode(result)
    file = open(image_url, 'wb')
    file.write(imgdata)
    file.close()
import os
def test(filename):
    image1 = "timg.jpg"
    image2 = filename
    image = filename
    try:
        merge_face(image2,image1,image,90)
    except:
        pass
test('./Cache/1.jpg')
# def main():
#     # test('./Cache/8.jpg')
#     for root,dir,files in os.walk('./Cache'):
#         for file in files:
#             filename = os.path.join(root,file)
#             # print(filename)
#             test(filename)


# print(os.path.split('./Cache\95.jpg'))

# test()