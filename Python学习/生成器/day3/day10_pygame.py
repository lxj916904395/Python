#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pygame

# def main():
#
#     # 初始化
#     pygame.init()
#
#     # 初始化窗口及尺寸
#     screen = pygame.display.set_mode((800, 600))
#     # 标题
#     pygame.display.set_caption('大球吃小球')
#
#     # 窗口背景色
#     screen.fill((255, 255, 255))
#
#     # 通过指定的文件名加载图像
#     ball_image = pygame.image.load('./test.jpg')
#
#     # 在窗口上渲染图像（参数分别是：加载的图片对象，图像的x、y值）
#     screen.blit(ball_image, (150, 150))
#
#
#     # 绘制一个圆(参数分别是: 屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
#     pygame.draw.circle(screen, (255, 0, 0), (300, 300), 30, 0)
#
#     # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
#     pygame.display.flip()
#
#     running = True
#
#     x, y = (50, 50)
#
#     # 开启循坏
#     while running:
#         # 从循环获取事件并处理
#         for event in pygame.event.get():
#
#             if event.type == pygame.QUIT:
#                 running = False

# """动画"""
# def main():
#     # 初始化导入的pygame中的模块
#     pygame.init()
#     # 初始化用于显示的窗口并设置窗口尺寸
#     screen = pygame.display.set_mode((800, 600))
#     # 设置当前窗口的标题
#     pygame.display.set_caption('大球吃小球')
#     # 定义变量来表示小球在屏幕上的位置
#     x, y = 50, 50
#     running = True
#     # 开启一个事件循环处理发生的事件
#     while running:
#         # 从消息队列中获取事件并对事件进行处理
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#         screen.fill((255, 255, 255))
#         pygame.draw.circle(screen, (255, 0, 0,), (x, y), 30, 0)
#         pygame.display.flip()
#         # 每隔50毫秒就改变小球的位置再刷新窗口
#         pygame.time.delay(50)
#         x, y = x + 5, y + 5

from enum import Enum, unique
from random import randint
from math import sqrt


@unique
class Color(Enum):
    """颜色"""
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """随机色"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):
    """求"""
    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        self._x = x
        self._y = y
        self._radius = radius
        self._sx = sx
        self._sy = sy
        self._color = color
        self._alive = True

    def move(self, screen):
        """移动"""

        self._x += self._sx
        self._y += self._sy

        if self._x - self._radius <= 0 or \
            self._x + self._radius >= screen.get_width():
            self._sx = - self._sx

        if self._y - self._radius <= 0 or \
            self._y + self._radius >= screen.get_height():
            self._sy = -self._sy

    def eat(self, other):
        """吃其他球"""
        if self._alive and other._alive and self != other:
            dx, dy = self._x - other._x, self._y - other._y
            distance = sqrt(dx ** 2 + dy ** 2)

            if distance < self._radius + other._radius \
                    and self._radius > other._radius:
                other._alive = False

                self._radius = self._radius + int(other._radius * 0.146)


    def draw(self, screen):
        """绘制"""
        pygame.draw.circle(screen, self._color, (self._x, self._y), self._radius, 0)



def exit():
    pass

def main():

    # 所有球的容器
    balls = []

    pygame.init()

    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('大球吃小球')

    runing = True

    while runing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False

            # 鼠标事件
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                ball = Ball(x, y, radius, sx, sy, color)
                balls.append(ball)

        screen.fill((255, 255, 255))

        for ball in balls:
            if ball._alive:
                ball.draw(screen)
            else:
                balls.remove(ball)

        pygame.display.flip()
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            for othetr in balls:
                ball.eat(othetr)


if __name__ == '__main__':
    main()