#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import chardet

# encoding：编码方式
# confidence：检测率
# language：语言

def main():
    res = chardet.detect(b'Hello world')
    print(res)
    # {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
    print()

    res = chardet.detect('离离原上草，一岁一枯荣'.encode('gbk'))
    print(res)
    #{'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}
    print()

    res = chardet.detect('离离原上草，一岁一枯荣'.encode('utf-8'))
    print(res)
    #{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
    print()

    res = chardet.detect('最新の主要ニュース'.encode('euc-jp'))
    print(res)
    #{'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}
    print()

    data = '灰烬之灵'.encode('gbk')
    res = chardet.detect(data)
    print(res)
    # {'encoding': None, 'confidence': 0.0, 'language': None}


if __name__ == '__main__':
    main()