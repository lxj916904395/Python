#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import socket, time
import threading

def init_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 监听本地回环地址
    s.bind(('127.0.0.1', 9999))

    # 开始监听
    # 5：最大监听数
    s.listen(5)
    print('wating for connection...')

    while True:
        # 接受新的连接
        sock, addr = s.accept()
        # 创建新线程处理tcp连接：
        t = threading.Thread(target=tcplink, args={sock, addr})
        t.start()


def tcplink(sock, addr):
    # print('Accept new connection from %s' % addr)
    sock.send(b'Welcome!')

    while True:
        data = sock.recv(1024).decode('utf-8')
        time.sleep(1)

        if not data or data == 'exit':
            break


        print('收到数据：', data)

        text = ('Hello,%s!' % data).encode('utf-8')
        print('发送数据：', text)
        sock.send(text)

    sock.close()
    print('Connection from %s:%s closed.' % addr)


if __name__ == '__main__':
    init_socket()