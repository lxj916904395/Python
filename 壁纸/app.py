#!/usr/bin/env python 
# -*- coding:utf-8 -*-

'''
制作iPhone x 猫耳朵壁纸
'''
from PIL import Image

# 原图片
img1 = Image.open('bz.jpeg')
img1 = img1.convert('RGBA')

# mask图片
mask = Image.open('mask.jpg')
mask = mask.convert('RGBA')

# 获取原图片尺寸
size = mask.size
# 制作猫儿图片
new_img = img1.resize(size)
img = Image.alpha_composite(new_img, mask)
img.save('bak.png')