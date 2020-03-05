#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 21:01
# @Author  : Xuegod Teacher For
# @File    : test.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import base64
from PIL import Image
from aip import AipOcr


# 破解携程反爬验证
class unlockScrapy(object):

    def __init__(self, driver):
        super(unlockScrapy, self).__init__()
        # selenium驱动
        self.driver = driver
        self.WAPPID = '百度文字识别appid'
        self.WAPPKEY = '百度文字识别appkey'
        self.WSECRETKEY = '百度文字识别secretkey'
        # 百度文字识别sdk客户端
        self.WCLIENT = AipOcr(self.WAPPID, self.WAPPKEY, self.WSECRETKEY)

    # 按顺序点击图片中的文字
    def clickWords(self, wordsPosInfo):
        # 获取到大图的element
        imgElement = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[3]/img")
        # 根据上图文字在下图中的顺序依次点击下图中的文字
        for info in wordsPosInfo:
            ActionChains(self.driver).move_to_element_with_offset(
                to_element=imgElement, xoffset=info['location']['left'] + 20,
                yoffset=info['location']['top'] + 20).click().perform()
            time.sleep(1)

    # 下载上面的小图和下面的大图
    def downloadImg(self):
        # 小图的src
        codeSrc = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[1]/img").get_attribute("src")
        # 大图的src
        checkSrc = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[3]/img").get_attribute("src")
        # 保存下载
        fh = open("code.jpeg", "wb")
        # 由于其src是base64编码的，因此需要以base64编码形式写入
        fh.write(base64.b64decode(codeSrc.split(',')[1]))
        fh.close()
        fh = open("checkCode.jpeg", "wb")
        fh.write(base64.b64decode(checkSrc.split(',')[1]))
        fh.close()

    # 图片二值化，便于识别其中的文字
    def chageImgLight(self):
        im = Image.open("code.jpeg")
        im1 = im.point(lambda p: p * 4)
        im1.save("code.jpeg")
        im = Image.open("checkCode.jpeg")
        im1 = im.point(lambda p: p * 4)
        im1.save("checkCode.jpeg")

    # 破解滑动
    def unlockScroll(self):
        # 滑块element
        scrollElement = self.driver.find_elements_by_class_name(
            'cpt-img-double-right-outer')[0]
        ActionChains(self.driver).click_and_hold(
            on_element=scrollElement).perform()
        ActionChains(self.driver).move_to_element_with_offset(
            to_element=scrollElement, xoffset=30, yoffset=10).perform()
        ActionChains(self.driver).move_to_element_with_offset(
            to_element=scrollElement, xoffset=100, yoffset=20).perform()
        ActionChains(self.driver).move_to_element_with_offset(
            to_element=scrollElement, xoffset=200, yoffset=50).perform()

    # 读取图片文件
    def getFile(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    # 识别上面小图中的文字
    def iTow(self):
        try:
            op = {'language_type': 'CHN_ENG', 'detect_direction': 'true'}
            res = self.WCLIENT.basicAccurate(
                self.getFile('code.jpeg'), options=op)
            words = ''
            for item in res['words_result']:
                if item['words'].endswith('。'):
                    words = words + item['words'] + '\r\n'
                else:
                    words = words + item['words']
            return words
        except:
            return 'error'

    # 识别下面大图中文字的坐标
    def getPos(self, words):
        try:
            op = {'language_type': 'CHN_ENG', 'recognize_granularity': 'small'}
            res = self.WCLIENT.accurate(
                self.getFile('checkCode.jpeg'), options=op)
            # 所有文字的位置信息
            allPosInfo = []
            # 需要的文字的位置信息
            needPosInfo = []
            for item in res['words_result']:
                allPosInfo.extend(item['chars'])
            # 筛选出需要的文字的位置信息
            for word in words:
                for item in allPosInfo:
                    if word == item['char']:
                        needPosInfo.append(item)
            return needPosInfo
        except Exception as e:
            print(e)

    def main(self):
        # 破解滑块
        self.unlockScroll()
        time.sleep(2)
        # 下载图片
        self.downloadImg()
        time.sleep(2)
        # 图像二值化，方便识别
        self.chageImgLight()
        # 识别小图文字
        text = self.iTow()
        # 获取大图的文字位置信息
        posInfo = self.getPos(list(text))
        # 由于小图或大图文字识别可能不准确，因此这里设置识别出的文字少于4个则重新识别
        while len(posInfo) != 4 or len(text) != 4:
            # 点击重新获取图片，再次识别
            self.driver.find_elements_by_xpath(
                '/html/body/div[3]/div[4]/div/a')[0].click()
            time.sleep(2)
            self.downloadImg()
            time.sleep(2)
            text = self.iTow()
            posInfo = self.getPos(list(text))
        time.sleep(3)
        print('匹配成功，开始点击')
        # 点击下面大图中的文字
        self.clickWords(posInfo)
        # 点击提交按钮
        self.driver.find_elements_by_xpath(
            '/html/body/div[3]/div[4]/a')[0].click()
        time.sleep(2)
        # 如果破解成功，html的title会变
        if self.driver.title != '携程在手，说走就走':
            print('破解成功')
        else:
            # 再次尝试
            print('破解失败，再次破解')
            self.main()


def unlock():
    driver = webdriver.Chrome()
    # 打开Chrome浏览器，需要将Chrome的驱动放在当前文件夹
    driver.get(
        'https://hotels.ctrip.com/hotel/6278770.html#ctm_ref=hod_hp_hot_dl_n_2_7')
    # 开始破解
    unlock = unlockScrapy(driver)
    unlock.main()

if __name__ == '__main__':
    unlock()



