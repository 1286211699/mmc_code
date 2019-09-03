import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait #
import os
if os.path.exists('1.txt'):
    os.remove('1.txt')


driver = webdriver.Chrome()
#
driver.implicitly_wait(30)
driver.get("https://www.baidu.com")
#显示等待
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "kw")))
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()

def parse_data(e_item):
    with open('1.txt','a',encoding='utf-8') as f:
        for e in e_item:
            print(e.find_element_by_tag_name('a').text)
            f.write(e.find_element_by_tag_name('a').text+'\n')

def main():
    for i in range(1,5):
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "su")))
        e_item = driver.find_elements_by_xpath('//div[@class="result c-container "]')
        parse_data(e_item)
        driver.find_element_by_xpath(f"//div[@id='page']/descendant::span[text()='{i}']").click()


if __name__ == '__main__':
    main()
    driver.quit()
