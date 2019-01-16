#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import hashlib

"""MD5，结果是固定的128 bit字节，通常用一个32位的16进制字符串表示"""

md5 = hashlib.md5()
md5.update('lxj'.encode('utf-8'))

# 等价于
# md5.update('l'.encode('utf-8'))
# md5.update('x'.encode('utf-8'))
# md5.update('j'.encode('utf-8'))

md5_str = md5.hexdigest()
print(md5_str)

"""SHA1,结果是160 bit字节，通常用一个40位的16进制字符串表示"""
sha1 = hashlib.sha1()
sha1.update('lxj'.encode('utf-8'))
sha1_str = sha1.hexdigest()
print(sha1_str)

