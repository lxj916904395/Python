#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 9999))


while True:
    data = s.recv(1024).decode('utf-8')
    if data:
        print('收到数据:', data)
        inputext = input('输入要发送的文字：')
        s.send(bytes(inputext, encoding='utf8'))

s.close()