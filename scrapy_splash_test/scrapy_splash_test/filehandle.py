#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os, requests

base_url = os.getcwd() + '/scrapy_splash_test/resources/'

"""创建文件"""

def mkdir(path):
    path = base_url + path
    if not os.path.exists(path):
        os.mkdir(path)


def save_pic(url, path):
    path = base_url + path
    content = requests.get(url)
    with open(path, 'wb') as f:
        f.write(content.content)