#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from time import time,sleep
from multiprocessing import Process
from os import getpid
from random import randint
from threading import Thread

class Pross_test:
    def download_task(self, filenale):
        print('开始下载 :%s== %d' % (filenale, getpid()))
        time_t = randint(4, 19)
        sleep(time_t)
        print('%s下载完成! 耗费了%d秒' % (filenale, time_t))

    def start_download(self):
        start = time()

        # 通过Process类创建了进程对象，通过target参数我们传入一个函数来表示进程启动后要执行的代码，
        # 后面的args是一个元组，它代表了传递给函数的参数
        p1 = Process(target=self.download_task, args=('泷泽萝拉.mp4',))
        # start方法用来启动进程
        p1.start()

        p2 = Process(target=self.download_task, args=('苍井空.mp4',))
        p2.start()

        # join方法表示等待进程执行结束
        p1.join()
        p2.join()

        end = time()

        print('总共耗费了%.2f秒.' % (end - start))




"""线程"""
class Thread_test:

    def download_task(self, filenale):
        print('开始下载 :%s== %d' % (filenale, getpid()))
        time_t = randint(4, 19)
        sleep(time_t)
        print('%s下载完成! 耗费了%d秒' % (filenale, time_t))

    def start_download(self):

        start = time()

        # 创建线程
        t1 = Thread(target=self.download_task, args=('饭岛爱.mp4',))
        # 启动线程
        t1.start()

        # 创建线程
        t2 = Thread(target=self.download_task, args=('哈哈谁啦.mp4',))
        # 启动线程
        t2.start()


        t1.join()
        t2.join()

        end = time()

        print('总共耗费了%.2f秒.' % (end - start))


"""自定义线程"""
class DownloadThread(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename


    def run(self):
        print('开始下载:%s' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))


if __name__ == '__main__':

    # p = Pross_test()
    # p.start_download()
    #
    #
    # t = Thread_test()
    # t.start_download()


    d = DownloadThread('xxx.mp4')
    d.start()