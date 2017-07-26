#!/usr/bin/env python
#coding=utf-8

import sys
import pyocr
from pyocr import pyocr
from PIL import Image
from PIL import ImageEnhance
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True,help = "Path to image")
args = vars(ap.parse_args())




tools = pyocr.get_available_tools()[:]
if len(tools) == 0:
    print("no ocr tool found")
    sys.exit(1)
else:
    print("Using '%s' " % (tools[0].get_name()))
img = Image.open(args['image'])


#img = img.resize((200,48), Image.ANTIALIAS) #图片放大
#img = ImageEnhance.Color(img).enhance(0.1) #颜色变为黑白
#img = ImageEnhance.Brightness (img).enhance(2.0) #亮度提高
#img = ImageEnhance.Contrast (img).enhance(2.0) #增强对比度
#img = ImageEnhance.Sharpness (img).enhance(3.0) #增加图像锐度



print(tools[0].image_to_string(img))