#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
from threading import Thread

class DownloadTask(Thread):

    def __init__(self, url):
        super().__init__()
        self._url = url


    def run(self):

        filename = self._url[self._url.rfind('/')+1:]

        # 获取网络资源
        resp = requests.get(self._url)

        # 文件写入
        with open('./images/'+filename, 'wb') as f:
            f.write(resp.content)


def main():

    resp = requests.get('http://api.tianapi.com/meinv/?key=30d4e6b06a41a7f1739ce117a2b3bfb0&num=10')

    data_model = resp.json()

    for dict in data_model['newslist']:
        url = dict['picUrl']
        # 下载资源
        DownloadTask(url).start()


if __name__ == '__main__':
    main()