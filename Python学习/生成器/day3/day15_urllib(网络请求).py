#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from urllib import request, parse
import ssl
import json

context = ssl._create_unverified_context()

def request_get1():
    with request.urlopen('https://api.douban.com/v2/book/2129650', context=context) as f:
        # 响应报文
        data = f.read()
        data_str = data.decode('utf-8')
        # 请求状态、状态解释
        print('Status:', f.status, f.reason)
        # 响应头
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))

        # 转化成dict
        json_dict = json.loads(data_str)
        # 遍历dict
        for k, v in json_dict.items():
            print(k, '==', v)



def request_get2():
    req = request.Request('https://www.baidu.com/')
    # 添加请求头
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

    with request.urlopen(req, context=context) as f:
        print('result:', f.status, f.reason)
        data = f.read()
        json_str = data.decode('utf-8')
        print(json_str)

def request_post():
    email = input('Email: ')
    passwd = input('Password: ')

    # 构造请求参数
    login_data = parse.urlencode([
        ('username', email),
        ('password', passwd),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])

    req = request.Request('https://passport.weibo.cn/sso/login')
    # 添加请求头
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer',
                   'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

    with request.urlopen(req, context=context, data=login_data.encode('utf-8')) as f:
        # 响应状态码
        print('Status:', f.status, f.reason)
        # 响应头
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        # 响应体
        print('Data:', f.read().decode('utf-8'))


def main():
    # request_get2()

    request_post()

if __name__ == '__main__':
    main()