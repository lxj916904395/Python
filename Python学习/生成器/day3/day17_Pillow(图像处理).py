#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from PIL import Image, ImageFilter

# 打开一个图片文件
im = Image.open('./images/test.jpg')

"""图片缩放"""


def image_thumbnail():
    # 获取图像的尺寸
    w, h = im.size

    print('缩放前图像宽：%s,图像高：%s' % (w, h))

    # 缩放到50%
    im.thumbnail((w // 2, h // 2))

    # 获取图像的尺寸
    w, h = im.size

    print('缩放后图像宽：%s,图像高：%s' % (w, h))

    # 保存为新的图像
    im.save('./images/test_thumbnail.jpg', 'jpeg')


"""图片模糊效果"""


def image_filter():
    # 应用模糊滤镜
    im2 = im.filter(ImageFilter.BLUR)
    # 保存图像
    im2.save('./images/test_filter.jpg', 'jpeg')


"""图片旋转"""


def image_rotate():
    # 180:旋转角度，默认逆时针旋转
    im2 = im.rotate(180)
    # 保存图像
    im2.save('./images/test_rotate.jpg', 'jpeg')


"""图像切片"""


def image_split():
    # 返回一个包含3张图像的元组，其色值分别为RGB中的一种
    im2 = im.split()
    # 保存图像
    for x in range(len(im2)):
        name = './images/test_split_%s.jpg' % x
        im2[x].save(name, 'jpeg')


def image_getchannel():
    for x in range(3):
        # getchannel（）其实是把split()返回的三张图片取出来按下标取出
        # 0：返回只包含RGB中R色值的图像
        # 1：返回只包含RGB中G色值的图像
        # 2：返回只包含RGB中B色值的图像
        im2 = im.getchannel(x)
        name = './images/test_getchannel_%s.jpg' % x
        im2.save(name, 'jpeg')




def main():
    # image_thumbnail()
    # image_filter()
    # image_rotate()
    # image_split()
    image_getchannel()


if __name__ == '__main__':
    main()
