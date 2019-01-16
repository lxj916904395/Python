#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import cv2

def detect(filename):
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

    img = cv2.imread(filename)

    # 灰度处理
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 人脸检测,每次迭代图像压缩率、人脸矩形保留近邻数目最小值

    faces = face_cascade.detectMultiScale(gray, 2, 2)

    # x,y为左上角坐标，w,h表示人脸宽度和高度

    for (x, y, w, h) in faces:
        # 检测到人脸绘制成蓝色矩形
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (225, 0, 0), 2)

    cv2.imwrite('./test_gray.jpeg', img)


filename = 'test.jpeg'
detect(filename)