#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os,time, random
from multiprocessing import Queue,Process
import multiprocessing
import threading

def write(q):
    print('Progress to write:%s' % os.getpid())
    for v in ['A', 'B', 'C']:
        print('Put %s to queue...' % v)
        q.put(v)
        time.sleep(random.random())


def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)



if __name__ == '__main__':
    q = Queue()

    w = Process(target=write, args=(q,))
    r = Process(target=read, args=(q,))

    w.start()
    r.start()

    r.terminate()
