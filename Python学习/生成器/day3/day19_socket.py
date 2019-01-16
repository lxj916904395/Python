#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import socket

# 创建socket对象
# AF_INET：指定使用ipv4协议
# SOCK_STREAM：指定使用面向流的TCP协议
# SOCK_DGRAM ：UDP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 建立连接
s.connect(('www.sina.com.cn', 80))

# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []
while True:
    # 每次最多接收1k个字节的数据
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

# 关闭连接
s.close()

data = b''.join(buffer)
print(data)

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

# 文件写入
with open('./resources/sina.html', 'wb') as f:
    f.write(html)