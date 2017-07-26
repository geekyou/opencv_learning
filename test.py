# -*- coding: utf-8 -*-
import sys


import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

#检查OCR库和工具
try:
    from pyocr import pyocr
    from PIL import Image
    from PIL import ImageEnhance
except ImportError:
    print ('模块导入错误,请使用pip安装,pytesseract依赖以下库：')
    print ('http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil')
    print ('http://code.google.com/p/tesseract-ocr/')
    raise SystemExit
tools = pyocr.get_available_tools()[:]
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)


#裁剪图片
FOLDER = ".\saved\\" #处理后的图片文件夹
FIN_IMAGE = 'x.png' #处理后的图片文件名
_CONTENT_TYPES = {'image/png': '.png', 'image/gif': '.gif', 'image/jpeg': '.jpg', 'image/jpeg': '.jpeg'}

FIN_IMAGE_PATH = FOLDER + FIN_IMAGE #处理后的图片保存路径
IMAGE_ORIG = "test.png" #原图路径
IMAGE_X1 = 105
IMAGE_Y1 = 252
IMAGE_X2 = 150
IMAGE_Y2 = 263
img_orig = Image.open(IMAGE_ORIG)  # 打开图片句柄
box = (IMAGE_X1, IMAGE_Y1, IMAGE_X2, IMAGE_Y2)  # 设定裁剪区域
img = img_orig.crop(box)  # 裁剪图片，并获取句柄region

#图片增强
img = img.resize((200,48), Image.ANTIALIAS) #图片放大
img = ImageEnhance.Color(img).enhance(0.1) #颜色变为黑白
img = ImageEnhance.Brightness (img).enhance(2.0) #亮度提高
img = ImageEnhance.Contrast (img).enhance(2.0) #增强对比度
img = ImageEnhance.Sharpness (img).enhance(3.0) #增加图像锐度
img.save(FOLDER + FIN_IMAGE)


#识别图片
# print("Using '%s'" % (tools[0].get_name()))
print (tools[0].image_to_string(Image.open('saved\\x.png'),lang='eng'))
# print tools[0].image_to_string(Image.open('saved\\x.png'),lang='chi_sim')

os.remove(FOLDER + FIN_IMAGE)

