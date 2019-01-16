#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from PIL import ImageDraw, ImageFilter, ImageFont, Image
import random

"""随机验证码"""

class MyImageDraw:
    # 随机字母
    def rndChar(self):
        return chr(random.randint(65, 90))

    # 随机颜色
    def rndColor(self):
        return (random.randint(64, 255),
                random.randint(64, 255),
                random.randint(64, 255))

    # 随机颜色2:
    def rndColor2(self):
        return (random.randint(32, 127),
                random.randint(32, 127),
                random.randint(32, 127))

    def image_draw(self):
        width = 60 * 4
        height = 60
        # 创建图片
        image = Image.new('RGB', (width, height), (255, 255, 255))
        # 创建字体
        font = ImageFont.truetype('Arial.ttf', 36)
        # 创建绘制对象
        draw = ImageDraw.Draw(image)
        # 绘制像素点
        for x in range(width):
            for y in range(height):
                draw.point((x, y), fill=self.rndColor())

        # 绘制文字
        for t in range(4):
            draw.text((60 * t + 10, 10),
                      self.rndChar(),
                      font=font,
                      fill=self.rndColor2())
        # 模糊效果
        image = image.filter(ImageFilter.BLUR)
        image.save('./images/test_code.jpg', 'jpeg')



def main():
    MyImageDraw().image_draw()


if __name__ == '__main__':
    main()