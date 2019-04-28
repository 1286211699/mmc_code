# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 10:09
# @Author  : for 
# @File    : 01_pil_test.py
# @Software: PyCharm
from PIL import Image
import pytesseract
img = Image.open('13.png')

img = img.convert('L')
#tesseract
result = pytesseract.image_to_string(img)

print(result)