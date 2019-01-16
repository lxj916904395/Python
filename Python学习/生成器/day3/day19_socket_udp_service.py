#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。
# 但是，能不能到达就不知道了。
#
# 虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。

import socket, threading

# SOCK_DGRAM：udp连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 监听本地回环地址
s.bind(('127.0.0.1', 9999))

while True:
    data, addr = s.recvfrom(1024)
    print('收到数据:', data.decode('utf-8'))

