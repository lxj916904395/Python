#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from turtle import *

def test1(wid, height):
    # 笔刷宽度
    width(4)

    # 前进
    forward(wid)

    # 右转90
    right(90)

    wid = wid - 4
    height = height - 4

    # 笔刷颜色
    pencolor('red')
    forward(height)
    right(90)

    pencolor('green')
    forward(wid)
    right(90)

    wid = wid - 4
    height = height - 4

    pencolor('blue')
    forward(height)
    right(90)

    test1(wid, height)

    if wid <= 80 or height <= 80:
        # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
        done()

def drawStar(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading: 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)

def begain_drawStar():
    for x in range(0, 250, 50):
        drawStar(x, 0)
    done()



if __name__ == '__main__':
    test1(200, 100)
    # begain_drawStar()