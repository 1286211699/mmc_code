from selenium import  webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait #

class DouyuSpider:
    def __init__(self):
        self.start_url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome()

    def get_content_list(self):

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "DyListCover-intro")))
        li_list = self.driver.find_elements_by_xpath("//ul[@class='layout-Cover-list']/li//h3")
        # print(li_list)
        content_list = []
        for li in li_list:
            print(li.text)

            # item = {}
        #
        #     # item["room_img"]=li.find_element_by_class_name("DyListCover-zone").text
        #     # item["room_img"]=li.find_element_by_xpath(".//span[@class='LazyLoad is-visible DyImg DyListCover-pic']/img").get_attribute("src")
        #     item["room_title"] = li.find_element_by_xpath(".//h3").text
        #     # item["room_cate"] = li.find_element_by_xpath('//*[@id="listAll"]/section[2]/div[2]/ul/li[5]/div/a[1]/div[2]/div[2]/span').text
        #     # item["anchor_name"] = li.find_element_by_xpath(".//h2[@class='DyListCover-user']").text
        #     # item["watch_num"] = li.find_element_by_xpath(".//span[@class='DyListCover-hot']").text
        #     # print(item)
        #     content_list.append(item)
        #隐世等待
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "dy-Pagination-item-custom")))
        next_url = self.driver.find_element_by_xpath('//span[contains(text(),"下一页")]')
        next_url = next_url if next_url else None
        return content_list,next_url

    def save_content_list(self,content_list):
        pass


    def run(self):#实现主要逻辑
        #1.start_url
        #2.发送请求，获取响应
        self.driver.get(self.start_url)
        #3.提取数据，提取下一页的元素
        content_list,next_url = self.get_content_list()
        time.sleep(30)
        #4.保存数据
        self.save_content_list(content_list)
        #5.点击下一页元素，循环
        # while next_url is not None:
        #     next_url.click()
        #     time.sleep(30)
        #     '''重复3,4操作'''
        #     content_list,next_url = self.get_content_list()
        #     self.save_content_list(content_list)


if __name__ == '__main__':
    douyu = DouyuSpider()
    douyu.run()
